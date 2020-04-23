# game component class

# imports
from random import shuffle

from data.myclasses import MyFrame, MyLabel, MyButton, MyQuestion

from data.myvariables import dev, colors


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

        self.game_bf = MyFrame(self.parent, colors[4])

    def create_end_frame(self):
        if dev:
            print '[game] end frame created'

        self.end_frame = MyFrame(self.game_bf.frame, colors[4])

        self.end_label = MyLabel(self.end_frame.frame,
                                 'You have gone through all the questions \n '
                                 'Please check in later for more \n '
                                 'Press "Escape" to exit',
                                 0.25, 0.25
                                 )
        self.end_label.label.configure(bg=colors[4], fg=colors[0])
        self.end_label.label.place(relwidth=0.50, relheight=0.15)

        self.score_button = MyButton(self.end_frame.frame, 'Calculate Score', self.calc_score, 0.45, 0.45)

    def create_questions(self):
        if dev:
            print '[game] questions created'

        self.q1 = MyQuestion(self.game_bf.frame,
                             'What is the moment of inertia, I for a disc?',
                             'I = MR^2',
                             'I = 1/12 *  ML^2',
                             'I = 1/2 *  MR^2',
                             'I = 1/2 *  Mk^2',
                             'This is the Moment of Inertia for a particle.',
                             'This is the Moment of Inertia for a stick.',
                             'This is the Moment of Inertia for a disc.',
                             'This Moment of Inertia is for a particle of a disc and involves k, \nwhich is the radius of gyration.',
                             3
                             )

        self.q2 = MyQuestion(self.game_bf.frame,
                             'What is the Rotational Kinetic Energy of a rolling disc?',
                             '0.5 * mv^2',
                             '0.25 * mr^2w^2',
                             '0.5 * mr^2',
                             '0.25 * Iw^2',
                             'This is a formula for Linear Kinetic Energy.',
                             'For a rolling disc, the Rotational Kinetic Energy is given as, \nRKE = 0.5 * Iw^2 = 0.5 * (0.5 * mr^2)w^2 = 0.25 * mr^2w^2 ',
                             'This is the Moment of Inertia of a disc. \nNote: This formula does not involve any kind of velocity. \nThus, it cannot be Kinetic Energy.',
                             'For a rolling disc, the Rotational Kinetic Energy is given as, \nRKE = 0.5 * Iw^2. \n\nWhen the Moment of Inertia of the disc is substituted, \nthen only the 0.25 appear.',
                             2
                             )

        self.q3 = MyQuestion(self.game_bf.frame,
                             'What is the angular momentum, L for an orbiting particle?',
                             'L = mr^2w',
                             'L = mv',
                             'L = wr',
                             'L = mr^2',
                             'The angular momentum for an orbiting paticle is given as, \nL = Iw. \n\nThus, when the Moment of Inertia(I) of a disc is substituted, \nL = mr^2w ',
                             'Recall that LINEAR Momentum is the product of mass and velocity. \np = mv',
                             'This formula is used to find linear velocity. \nv = wr',
                             'This formula is the Moment of Inertia for a particle. \nI = mr^2',
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
                             'kgms^-1',
                             'kgm^2(s^-2)',
                             'kgm^2(s^-1)',
                             'kgm^2',
                             'This unit is for LINEAR Momentum. \nLinear and Angular Momentum have different units due to involving different quantities. \np = mv = kgms^-1',
                             'This unit is for Torque. \nTorque is the product of Moment of Inertia and Angular Acceleration. \nT = Ia = kgm^2(s^-2)',
                             'This is the unit for Angular Momentum. \nL = Iw = (MR^2)w = (kgm^2)s^-1',
                             'This is the unit for Moment of Inertia. \nI = mr^2 = kgm^2',
                             3
                             )

        self.q6 = MyQuestion(self.game_bf.frame,
                             'What real force keeps a satellite in a circular orbit around the earth?',
                             'Thrust',
                             'Gravity',
                             'Centripetal force',
                             'There is no force in space',
                             'This is a propulsive force. ',
                             'Gravitational pull of earth acts on the satellite which keeps the satellite in a circular orbit \naround the earth provided its velocity balances the gravitational force.',
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
                             'Centrifugal force is the tendency of an object to \nfly away from the center of a curved path.',
                             'Centripetal force is the net force keeping an object in circular motion. \nThe resultant force of all real forces acting on the object, \nthat acts towards the centre of the circular path is responsible for its circular motion.',
                             'This force is also called Centrifugal Force which is \nthe tendency of an object to fly away from the center of a curved path.',
                             'This is an attractive force which occurs between \nmasses of objects and it is not a net force.',
                             2
                             )

        # creating qlist
        self.qlist = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8]

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

    def calc_score(self):
        if not self.score_calulated:
            if dev:
                print '[game] calculating final score'

            # figuring out how many questions were correct:
            tmp_var = 0
            for question in self.qlist:
                if question.is_correct:
                    tmp_var += 1

            self.score_label = MyLabel(self.end_frame.frame,
                                       'You got ' + str(tmp_var) + '/' + str(len(self.qlist)) + ' questions correct!',
                                       0.25, 0.55
                                       )
            self.score_label.label.configure(bg=colors[4], fg=colors[0])
            self.score_label.label.place(relwidth=0.50, relheight=0.15)

            self.score_calulated = True
        else:
            return
