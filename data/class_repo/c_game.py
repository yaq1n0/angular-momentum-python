# game component class
# -*- encoding: utf-8 -*-

# imports
from Tkinter import N
from random import shuffle
from data.myvariables import dev, MyFonts
from data.myfunctions import GrayScale
from data.myclasses import MyFrame, MyLabel, MyButton, MyQuestion


class MyGameFrame(object):
    def __init__(self, parent):
        # assigning parameters to attributes
        self.parent = parent

        # creating frames
        self.create_game_bf()
        self.create_end_frame()

        # creating vars
        self.score_calulated = False

    def create_game_bf(self):
        if dev:
            print '[game] game base frame created'

        self.game_bf = MyFrame(self.parent, GrayScale(20))

    def create_end_frame(self):
        if dev:
            print '[game] end frame created'

        self.end_frame = MyFrame(self.game_bf.frame, GrayScale(80))

        self.end_label = MyLabel(self.end_frame.frame, 'You have finished the Quiz Game!', 0.25, 0.25)
        self.end_label.label.configure(font=MyFonts['ExtraLarge'], bg=GrayScale(80), fg=GrayScale(220))
        self.end_label.label.place(relwidth=0.50, relheight=0.15)

        self.score_button = MyButton(self.end_frame.frame, 'Calculate Score', self.calc_score, 0.45, 0.45)

        self.credits_label = MyLabel(self.end_frame.frame, 'Questions by:'
                                                           '\nLian Chao Hooi', 0.25, 0.85)

        self.credits_label.label.configure(bg=GrayScale(80), anchor=N, font=MyFonts['Default'])
        self.credits_label.label.place(relwidth=0.50)

    def create_questions(self):
        if dev:
            print '[game] questions created'

        self.q1 = MyQuestion(self.game_bf.frame,
                             'What is the moment of inertia, I for a disc?',
                             'I = MR²',
                             'I = ¹⁄₁₂ ML²',
                             'I = ½ MR²',
                             'I = ½ Mk²',
                             'This is the Moment of Inertia for a particle.',
                             'This is the Moment of Inertia for a stick.',
                             'This is the Moment of Inertia for a disc.',
                             'I = Mk² is the Moment of Inertia for a disc'
                             'involving k, radius of gyration.',
                             3
                             )

        self.q2 = MyQuestion(self.game_bf.frame,
                             'What is the Rotational Kinetic Energy of a rolling disc?',
                             '0.5 mv²',
                             '0.25 mr²w²',
                             '0.5 mr²',
                             '0.25 Iw²',
                             'This is a formula for Linear Kinetic Energy.',
                             'For a rolling disc, the Rotational Kinetic Energy is given as,'
                             'RKE = 0.5 Iw² = 0.5 (0.5 mr²)w² = 0.25 mr²w²',
                             'This is the Moment of Inertia of a disc.'
                             '\nNote: This formula does not involve any kind of velocity.'
                             'Thus, it cannot be Kinetic Energy.',
                             'For a rolling disc, the Rotational Kinetic Energy is given as,'
                             '\nRKE = 0.5 Iw².'
                             '\n\nWhen the Moment of Inertia of the disc is substituted,'
                             'then only the 0.25 appear.',
                             2
                             )

        self.q3 = MyQuestion(self.game_bf.frame,
                             'What is the angular momentum, L for an orbiting particle?',
                             'L = mr²w',
                             'L = mv',
                             'L = wr',
                             'L = mr²',
                             'The angular momentum for an orbiting paticle is given as,'
                             '\nL = Iw.'
                             '\n\nThus, when the Moment of Inertia(I) of a disc is substituted,'
                             '\nL = mr²w',
                             'Recall that LINEAR Momentum is the product of mass and velocity.'
                             '\np = mv',
                             'This formula is used to find linear velocity.'
                             '\nv = wr',
                             'This formula is the Moment of Inertia for a particle.'
                             '\nI = mr²',
                             1
                             )

        self.q4 = MyQuestion(self.game_bf.frame,
                             'Rate of change of angular momentum is equal to ___________?',
                             'torque',
                             'force',
                             'moment of inertia',
                             'angular velocity',
                             'Torque is the rate of change of angular momentum.',
                             'Force is the rate of change of LINEAR momentum.',
                             'Moment of Inertia is the product of mass and square of distance.',
                             'Angular Velocity is the rate of change of Angular Displacement in radians per second.',
                             1
                             )

        self.q5 = MyQuestion(self.game_bf.frame,
                             'What is the unit for Angular Momentum?',
                             'kgm/s',
                             'kgm²/s²',
                             'kgm²/s',
                             'kgm²',
                             'This unit is for LINEAR Momentum.'
                             'Linear and Angular Momentum have different units due to involving different quantities.'
                             '\np = mv = kgm/s',
                             'This unit is for Torque.'
                             'Torque is the product of Moment of Inertia and Angular Acceleration. '
                             '\nT = Ia = kgm²/s²',
                             'This is the unit for Angular Momentum.'
                             '\nL = Iw = (MR²)w = (kgm²/s',
                             'This is the unit for Moment of Inertia.'
                             '\nI = mr² = kgm²',
                             3
                             )

        self.q6 = MyQuestion(self.game_bf.frame,
                             'What real force keeps a satellite in a circular orbit around the earth?',
                             'Thrust',
                             'Gravity',
                             'Centripetal force',
                             'There is no force in space',
                             'This is a propulsive force.',
                             'Gravitational pull of earth acts on the satellite '
                             'which keeps the satellite in a circular orbit '
                             'around the earth provided its velocity balances the gravitational force.',
                             'Centripetal force is just a net force.',
                             'Gravitational force exists in space.',
                             2
                             )

        self.q7 = MyQuestion(self.game_bf.frame,
                             'The velocity is always __________ to the line of a circle.',
                             'tangent',
                             'towards the center',
                             'outwards',
                             'inwards',
                             'Velocity acts tangent to a circle.',
                             'Centripetal force acts towards the center of a circle.',
                             'Invalid answer.',
                             'Invalid answer.',
                             1
                             )

        self.q8 = MyQuestion(self.game_bf.frame,
                             'What is the force that keeps an object in circular motion?',
                             'Centrifugal force',
                             'Centripetal force',
                             'Center-fleeing force',
                             'Gravitational Force',
                             'Centrifugal force is the tendency of an object to '
                             'fly away from the center of a curved path.',
                             'Centripetal force is the net force keeping an object in circular motion. '
                             'The resultant force of all real forces acting on the object, '
                             'that acts towards the centre of the circular path is responsible for its circular motion.',
                             'This force is also called Centrifugal Force which is '
                             'the tendency of an object to fly away from the center of a curved path.',
                             'This is an attractive force which occurs between '
                             'masses of objects and it is not a net force.',
                             2
                             )

        self.q9 = MyQuestion(self.game_bf.frame,
                             'What is the moment of inertia, I for a particle?',
                             'I = MR²',
                             'I = ¹⁄₁₂ ML²',
                             'I = ½ MR²',
                             'I = ½ Mk²',
                             'This is the Moment of Inertia for a particle.',
                             'This is the Moment of Inertia for a stick.',
                             'This is the Moment of Inertia for a disc.',
                             'I = Mk² is the Moment of Inertia for a disc where k is the radius of gyration.',
                             1
                             )

        self.q10 = MyQuestion(self.game_bf.frame,
                              'What is the Rotational Kinetic Energy of an orbiting particle?',
                              '0.5 mv²',
                              '0.5 mr²w²',
                              '0.5 mr²',
                              '0.25 Iw²',
                              'This is a formula for Linear Kinetic Energy.',
                              'For an orbiting particle, the Rotational Kinetic Energy is given as,'
                              '\nRKE = 0.5 Iw² = 0.5 mr²w² ',
                              'This is the Moment of Inertia of a disc. '
                              '\nNote: This formula does not involve any kind of velocity.'
                              'Thus, it cannot be Kinetic Energy.',
                              'For a rolling disc, the Rotational Kinetic Energy is given as,'
                              '\nRKE = 0.5 Iw². '
                              '\n\nWhen the Moment of Inertia of the disc is substituted, '
                              'then only the 0.25 appear.',
                              2
                              )

        self.q11 = MyQuestion(self.game_bf.frame,
                              'What is the moment of inertia, I for a disc?',
                              'I = MR²',
                              'I = ¹⁄₁₂ ML²',
                              'I = ½ MR',
                              'I = Mk²',
                              'This is the Moment of Inertia for a particle.',
                              'This is the Moment of Inertia for a stick.',
                              '½ MR² is the Moment of Inertia for a disc instead of ½ MR.',
                              'This is the Moment of Inertia for a disc which involves k, '
                              'the radius of gyration.',
                              4
                              )

        self.q12 = MyQuestion(self.game_bf.frame,
                              'Rate of change of linear momentum is equal to ___________?',
                              'torque',
                              'force',
                              'moment of inertia',
                              'angular velocity',
                              'Torque is the rate of change of angular momentum.',
                              'Force is the rate of change of LINEAR momentum.',
                              'Moment of Inertia is the product of mass and square of distance.',
                              'Angular Velocity is the rate of change of Angular Displacement in radians per second.',
                              2
                              )

        self.q13 = MyQuestion(self.game_bf.frame,
                              'What is the unit for Moment of Inertia?',
                              'kgm/s',
                              'kgm²/s²',
                              'kgm²/s',
                              'kgm²',
                              'This unit is for LINEAR Momentum.'
                              '\nLinear and Angular Momentum have different units due to involving different quantities.'
                              '\np = mv = kgm/s',
                              'This unit is for Torque.'
                              'Torque is the product of Moment of Inertia and Angular Acceleration.'
                              '\nT = Ia = kgm²/s²',
                              'This is the unit for Angular Momentum.'
                              '\nL = Iw = (MR²)w = (kgm²)/s',
                              'This is the unit for Moment of Inertia.'
                              '\nI = mr² = kgm²',
                              4
                              )

        self.q14 = MyQuestion(self.game_bf.frame,
                              'What is the unit for Torque?',
                              'kgm/s',
                              'kgm²/s²',
                              'kgm²/s',
                              'kgm²',
                              'This unit is for LINEAR Momentum. '
                              'Linear and Angular Momentum have different units due to involving different quantities. '
                              '\np = mv = kgm/s',
                              'This unit is for Torque, '
                              'the product of Moment of Inertia and Angular Acceleration. '
                              '\nT = Ia = kgm²/s²',
                              'This is the unit for Angular Momentum.'
                              '\nL = Iw = (MR²)w = (kgm²)/s',
                              'This is the unit for Moment of Inertia.'
                              '\nI = mr² = kgm²',
                              2
                              )

        self.q15 = MyQuestion(self.game_bf.frame,
                              'What is the Linear Kinetic Energy of a rolling ball?',
                              '0.5 mv²',
                              '0.5 mr²w²',
                              '0.5 mr²',
                              '0.25 Iw²',
                              'This is a formula for Linear Kinetic Energy.',
                              'For an orbiting particle, the Rotational Kinetic Energy is given as,'
                              '\nRKE = 0.5 Iw² = 0.5 mr²w² ',
                              'This is the Moment of Inertia of a disc.'
                              '\nNote: This formula does not involve any kind of velocity. '
                              'Thus, it cannot be Kinetic Energy.',
                              'For a rolling disc, the Rotational Kinetic Energy is given as,'
                              '\nRKE = 0.5 Iw². '
                              '\n\nWhen the Moment of Inertia of the disc is substituted, '
                              'then only the 0.25 appear.',
                              1
                              )

        # creating qlist
        self.qlist = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9,
                      self.q10, self.q11, self.q12, self.q13, self.q14, self.q15]

    def shuffle_questions(self):
        if dev:
            print '[game] questions shuffled'

        shuffle(self.qlist)

        for question in self.qlist:
            question.pf.tkraise()

    def destroy_questions(self):
        if dev:
            print '[game] deleting questions'

        for question in self.qlist:
            question.pf.destroy()

        if self.score_calulated:
            self.score_label.label.destroy()
            self.score_calulated = False

    def calc_score(self):
        if not self.score_calulated:
            if dev:
                print '[game] calculating final score'

            # figuring out how many questions were correct:
            tmp_var = 0
            for question in self.qlist:
                if question.is_correct.get():
                    tmp_var += 1

            self.score_label = MyLabel(self.end_frame.frame,
                                       'You got ' + str(tmp_var) + '/' + str(len(self.qlist)) + ' questions correct!',
                                       0.25, 0.55
                                       )
            self.score_label.label.configure(font=MyFonts['LargeBold'], bg=GrayScale(80), fg=GrayScale(220))
            self.score_label.label.place(relwidth=0.50, relheight=0.15)

            self.score_calulated = True
        else:
            return
