class student
{
    String name, course;
    int roll;
    int maths, physics, chemistry, biology, english;

    student(String name, String course, int roll, int maths, int physics, int chemistry, int biology, int english) {
        this.name = name;
        this.roll = roll;
        this.course = course;
        this.maths = maths;
        this.physics = physics;
        this.chemistry = chemistry;
        this.biology = biology;
        this.english = english;
    }

    float average_marks() {
        return ((this.maths + this.physics + this.chemistry + this.biology + this.english) / 5);
    }
}

class student_info
{
    int laststudent = -1;
    student studentList[] = new student[10];

    student_info() {
    };

    void add(student newstudent) {
        boolean present = false;
        for (int i = 0; i <= laststudent; i++) {
            if (studentList[i].name == newstudent.name) {
                studentList[i].maths = newstudent.maths;
                studentList[i].physics = newstudent.physics;
                studentList[i].chemistry = newstudent.chemistry;
                studentList[i].biology = newstudent.biology;
                studentList[i].english = newstudent.english;
                present = true;
            }

        }
        if (present == false) {
            studentList[++laststudent] = newstudent;
        }
    }

    float student_wise_average() {
        float sum = 0;
        for (int i = 0; i <= laststudent; i++) {
            sum += studentList[i].maths + studentList[i].physics + studentList[i].chemistry + studentList[i].biology
                    + studentList[i].english;
        }
        return (sum / 5 + laststudent + 1);
    }

    float physics_avg() {
        int sum = 0;
        for (int i = 0; i <= laststudent; i++) {
            sum += studentList[i].physics;
        }
        return sum / (2);
    }

    float biology_avg() {
        int sum = 0;
        for (int i = 0; i <= laststudent; i++) {
            sum += studentList[i].biology;
        }
        return sum / (2);
    }

    float maths_avg() {
        int sum = 0;
        for (int i = 0; i <= laststudent; i++) {
            sum += studentList[i].maths;
        }
        return sum / (2);
    }

    float chemistry_avg() {
        int sum = 0;
        for (int i = 0; i <= laststudent; i++) {
            sum += studentList[i].chemistry;
        }
        return sum / (2);
    }

    float english_avg() {
        int sum = 0;
        for (int i = 0; i <= laststudent; i++) {
            sum += studentList[i].english;
        }
        return sum / (2);
    }
}

class Result
{
    public static void main(String args[]) {
        student s1 = new student("Souvik", "BSH", 9, 99, 56, 95, 80, 100);
        student s2 = new student("Soumi", "BSH", 2, 96, 56, 95, 100, 78);
        student_info class2 = new student_info();
        class2.add(s1);
        class2.add(s2);
        System.out.println("Average english marks: " + class2.english_avg());
        System.out.println("Average maths marks: " + class2.maths_avg());
        System.out.println("Average physics marks: " + class2.physics_avg());
        System.out.println("Average chemestry marks: " + class2.chemistry_avg());
        System.out.println("Average biology marks: " + class2.biology_avg());
        System.out.println("Average student marks: " + class2.student_wise_average());
    }
}