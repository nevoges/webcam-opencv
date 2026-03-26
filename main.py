import cv2
import sys

def main():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # CAP_DSHOW = faster init on Windows

    if not cap.isOpened():
        print("Error: Could not open webcam. Check that it's connected and not in use.")
        sys.exit(1)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("Webcam started. Press ESC to exit.")

    consecutive_failures = 0
    MAX_FAILURES = 10

    while True:
        ret, frame = cap.read()

        if not ret:
            consecutive_failures += 1
            print(f"Warning: Failed to grab frame ({consecutive_failures}/{MAX_FAILURES})")
            if consecutive_failures >= MAX_FAILURES:
                print("Error: Too many consecutive frame failures. Exiting.")
                break
            continue

        consecutive_failures = 0  # reset on success

        cv2.imshow("Webcam — ESC to exit", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # 27 = ESC
            print("ESC pressed. Exiting.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()