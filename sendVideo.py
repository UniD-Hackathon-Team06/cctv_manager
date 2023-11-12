import asyncio
import websockets
import base64


async def send_image():
    count_ = 0
    uri = "ws://ec2-43-201-77-177.ap-northeast-2.compute.amazonaws.com:8000/ws/1"
    async with websockets.connect(uri, max_size=3000000) as websocket:
        # 이미지 파일을 열어서 base64 인코딩

        while 1:
            with open(f'./images/output_image{count_}.png', "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
                print(encoded_image)

            try:
                # 서버로부터 처리된 이미지 데이터 수신
                await websocket.send(encoded_image)
                processed_image_data = await websocket.recv()
                print(processed_image_data)
            except websockets.exceptions.ConnectionClosedError:
                print("Connection closed unexpectedly. Reconnecting...")
                break

            await asyncio.sleep(0)

            print(processed_image_data)
            count_ += 6
            if count_ == 60:
                count_ = 0



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_image())