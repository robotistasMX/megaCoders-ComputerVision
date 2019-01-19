
//g++ $(pkg-config --cflags --libs opencv) -std=c++11  programaClase.cpp -o yourFileProgram
#include "opencv2/opencv.hpp"
using namespace cv;
int main(int, char**)
{
    Mat gray;
    Mat hsv;
    Mat mask;
    Mat filtro1, filtro2;
    double dM01, dM10, dArea;
    VideoCapture cap(0); 
    if(!cap.isOpened()) 
        return -1;

    for(;;)
    {
        Mat frame;
        cap >> frame; 
        cvtColor(frame, gray, COLOR_BGR2GRAY);
        imshow("Gray", gray);
        cvtColor(frame, hsv, COLOR_BGR2HSV);
        imshow("HSV", hsv);
        Scalar minBlue = cv::Scalar(98,99,87); 
        Scalar maxBlue = cv::Scalar(115,255,255); 
        inRange(hsv, minBlue, maxBlue, mask);
        imshow("blue", mask);
        erode(mask, filtro1, getStructuringElement(MORPH_RECT, Size(3, 3)) );
        erode(filtro1, filtro2, getStructuringElement(MORPH_RECT, Size(5, 5)) );

        Moments oMoments = moments(filtro2);
        dM01 = oMoments.m01;
        dM10 = oMoments.m10;
        dArea = oMoments.m00;
        if (dArea > 50000)
        {
            int posX = dM10 / dArea;
            int posY = dM01 / dArea;
            circle(frame, Point(posX,posY), 10, Scalar(0,255,0), 2);
        }
        imshow("frame", frame);
        if(waitKey(30) >= 0) break;
    }
    
    return 0;
}