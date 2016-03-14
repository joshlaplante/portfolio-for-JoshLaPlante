### Image Resize GUI
***
##### Challenge:
While taking a course on Python through The Tech Academy of Portland, I was prompted to design and develop a project of my choosing using Visual Studio's Python Tools. I decided to create a GUI that would allow users to easily resize images on their machine.

##### Action Taken:
I first drafted a model of the GUI's design and function, and after gaining approval from my instructor, began coding using Visual Studio's Python 3.4 tools. The GUI is built using Tkinter's themed widgets and the acual image handling is done through PIL. 

##### Result:
I am extremely pleased with my resulting GUI and its functionality! It has scalebars to resize both the height and width of a chosen image, and as a user drags the scalebar cursors, the image is resized in real-time within the GUI's display. The current dimensions of the image are displayed in the GUI as well. After resizing an image, a user can save it to their machine as a new file of the same data type as the original image. The one downside of my program is image size restraint--I had to limit the maximum pixel dimensions of the chosen image so that everything would properly display in the GUI without running off the screen. One feature I might add in the future is the option to keep the original image pixel ratio constant as the image is resized, so that users can resize images without stretching them too much vertically or horizontally. During this project I learned a lot about PIL, such as how powerful it is for image processing and how easily it can be applied to a GUI model like Tkinter. I had worked with Tkinter previously in this Python Course, but during this practical I learned about more features like retrieving the screen size of the monitor, linking variables to control widgets, and tweaking widget styles. One hurdle I had to overcome as I tested my GUI was image distortion after resizing a picture multiple times. Originally, each image resize created a new image from the image created by a previous resize, but this caused the images to stretch out and blur. Eventually I discovered how to create every sequential resized image from the original picture to prevent this and display much clearer images. I'm glad I got to make something useful for my practical as I've already used this application personally to resize some pictures on my computer! I would love any feedback or suggestions on my project.

***
[return to portfolio](https://github.com/joshlaplante/portfolio-for-JoshLaPlante)
