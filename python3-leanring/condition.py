class Condition:

    @classmethod
    def learncondition(cls, score, subject, name) -> str | None:
        cls.score = score
        level_message = cls.calculatescore(score,subject)
        level_title = cls.exam_whoami(name)
        level_message= level_message + level_title
        level_message = level_message + Condition.envinfo('jeffery','123456')
        return level_message

    @classmethod
    def calculatescore(cls, score, subject):
        score = int(score)
        subject = str(subject)

        subject_name  =  cls.subject(subject)

        if score < 60:
            return f'{subject_name} not pass the exam'
        elif score < 90:
            return f'{subject_name} pass the exam'
        elif score <=100:
            return f'prefect~ {subject_name} pass the exam, you are success!!!'

    @classmethod
    def subject(cls, sub) -> str | None:
        subject = {'a':'English', 'b':'Mathematics', 'c':'Chinese', 'd':'Physics','e':'Biology', 'f':'Geography', 'g':'History', 'm':'Music'}

        for key, value in subject.items():
            if value == sub:
                return key
            # else:
            #     return None

        return subject.get(sub)

    def exam_whoami(self) -> str | None:
        name = 'my name is jeffery'
        return name

    @staticmethod
    def envinfo(username, password) -> str | None:
        username = username.strip()
        password = password.strip()
        return  username + ' ' + password


# condition = Condition()
# test case
# score  =  input('请输入内容:')
# subject  =  input('请输入内容:')
# print(condition.subject(params))

# exam_student = Condition()
print(Condition.learncondition(99, 'a','jeffery'))

