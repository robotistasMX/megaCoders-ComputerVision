
//g++ $(pkg-config --cflags --libs opencv) -std=c++11  programaClase.cpp -o yourFileProgram
#include "opencv2/opencv.hpp"
using namespace cv;
int main(int, char**)
{
    int circulosMax = 5;
    circulosMax = circulosMax -1;
    vector<Vec3f> circles;
    Scalar min = cv::Scalar(0,0,66); 
    Scalar max = cv::Scalar(162,114,255);    
    Mat frame;
    Mat hsv;    
    Mat mask;
    Mat frame2;
    Mat filtro1, filtro2;
    
    VideoCapture cap(0); 
    if(!cap.isOpened()) 
        return -1;

    for(;;)
    {
        
        cap >> frame; 
        cvtColor(frame, hsv, COLOR_BGR2HSV);
        Scalar min = cv::Scalar(98,99,87); 
        Scalar max = cv::Scalar(115,255,255);

        inRange(hsv, min, max, mask);
        adaptiveThreshold(mask, ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,19,3)
 
        erode(frame2, filtro1, getStructuringElement(MORPH_RECT, Size(3, 3)) );
        dilate(filtro1, filtro2, getStructuringElement(MORPH_RECT, Size(3, 3)) );

        HoughCircles( filtro2, circles, CV_HOUGH_GRADIENT, 1, filtro2.rows/8, 200, 100, 5, 100 );
         for( int i = 0; i <circulosMax; i++ )
        {
            Vec3i c = circles[i];
            Point center = Point(c[0], c[1]);
            // circle center
            circle( frame, center, 1, Scalar(0,100,100), 3, LINE_AA);
            // circle outline
            int radius = c[2];
            circle( frame, center, radius, Scalar(255,0,255), 3, LINE_AA);
        }
        imshow("frame", frame);
        if(waitKey(30) >= 0) break;
    }
    
    return 0;
}