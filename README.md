# Recurrent-models-for-situation-recognition

The following project is a course project of the course GNR-638(IIT Bombay). It has been done under the guidance of Prof. Biplab Banerjee. The project includes a very basic implementation of the paper ***Recurrent Models for Situation Recognition***[1].
</br>**The project report consists of a broad explaination of the implementaions, results, and conclusion**. Recognition of actions and human-object interactions in still images has been widely studied in computer vision. Earlier the focus was on predicting only the verbs, now the focus has been shifted to more general things like what is being done, who is doing what, where it is being done. The recently introduced imSitu Dataset generalizes the task of action recognition to ‘situation recognition’, the recognition of all entities fulfilling semantic roles in an instance of an action performed by a human or non-human actor.

</br>We can see in the figure below that each image in imSitu data-set is labeled with an action verb (orange), and each verb is associated with a unique set of semantic roles (bold black) which are fulfilled by noun entities present in the image (green). Each image has multiple annotations to account for the intrinsic ambiguity of the task. Our approach first uses the fusion network to predict the action verb. Then it feeds the verb and a visual feature from a separate network(Noun Prediction network) into an RNN to predict the noun roles in a fixed sequence conditioned on the action.
**![](https://lh3.googleusercontent.com/ctELJP6I_UpZGRbwWUh2q7avoEbIiHds1yVBb4-L4X0TnU0gubCoPWNimce12cvKhJxcjq8RUtoKgW3GTGa8x4UXGNIOjLXroAx_sIPnc75nWAENn6C4_HJTF28KVW8cNKDArfe7)**

## Data-set
The data-set[imsitu] that has been used in the research paper and this project is imSitu data-set([link](http://imsitu.org/)). The total number of verbs are 504, with the total number of images 126,102. The situation per image are 3. The total number of annotations are 1,481,851. The other parametric information can be seen from figure below
**![](https://lh4.googleusercontent.com/BM5j3OLdUSA6mhH4tGmxb8uCJIltYgOevSPUav3TASdG1FC7zGwQkRCNE_y3jK7Cru3MSsQHQ4zmwscHkk4sqz-7ncoNKst-bhJQHTgCUGbTZe9q5XkgCV56ZdX4GFUZwd1eq3BL)**

</br> **The other details are explained broadly in the report**


[1] Mallya, Arun, and Svetlana Lazebnik. "Recurrent models for situation recognition." Proceedings of the IEEE International Conference on Computer Vision. 2017.
