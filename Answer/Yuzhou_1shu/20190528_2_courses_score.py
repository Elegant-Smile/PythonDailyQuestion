class Student:
    name = '姓名'
    course = 'none'
    course_score = -1

    def theHighestScore(self, course_score_list):
        return max(course_score_list)

    def theLowestScore(self, course_score_list):
        return min(course_score_list)

    def theAverageScore(self, course_score_list):
        sum = 0
        for score in course_score_list:
            sum += score

        average_score = sum / len(course_score_list)
        return average_score


if __name__ == '__main__':
    student = Student()
    student.name = '小明'

    course_score_dict = {}

    student.course = list(map(str, input("请先输入课程名:").strip().split()))
    student.course_score = list(map(float, input("然后请输入课程对应考试分数:").strip().split()))

    course_score_dict = dict(zip(student.course, student.course_score))

    print(course_score_dict)
    theHighestScore = student.theHighestScore(student.course_score)
    theLowestScore = student.theLowestScore(student.course_score)

    print('最高分课程是%s %d' % (max(course_score_dict, key=course_score_dict.get), theHighestScore))
    print('最低分课程是%s %d' % (min(course_score_dict, key=course_score_dict.get), theLowestScore))
    print('平均分是', student.theAverageScore(student.course_score))
