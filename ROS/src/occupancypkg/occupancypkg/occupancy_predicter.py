import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import requests


class OccupancyPredicter(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'driving_directory',
            self.listener_callback,
            10)
        self.subscription
        
        self.publisher_ = self.create_publisher(String, 'occupancy_data', 10)

    def listener_callback(self, msg):
        driving_directory = msg.data


        result = self.tpvformer_request(driving_directory)

        result_msg = String()
        result_msg.data = result
        self.publisher_.publish(result_msg)

    def tpvformer_request(self, dir):
        #data = {
        #    "directory": dir
        #}
        #response = requests.post(
        #    "https://api",
        #    data=data
        #)

        #return response.json()["directory"] # returned directory of occupancy data
        self.get_logger().info(f'I processed {dir}')
        return "./results/0"


def main(args=None):
    rclpy.init(args=args)

    occupancy_predicter = OccupancyPredicter()

    rclpy.spin(occupancy_predicter)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    occupancy_predicter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
