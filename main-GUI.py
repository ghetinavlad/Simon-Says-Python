import pygame
import time
import random

from minigamesSimonSays import *


class simon_says_GUI:
    def __init__(self):
        self.Window_Size = [800,600]
        self.Screen = 0
        self.Grey_ID = (253, 198, 202)
        self.Dark_Red_ID = (153, 0, 0)
        self.Light_Red_ID = (255, 0, 0)
        self.Dark_Green_ID = (1, 79, 0)
        self.Light_Green_ID = (0, 214, 102)
        self.Dark_Yellow_ID = (143, 178, 0)
        self.Light_Yellow_ID = (197, 255, 0)
        self.Dark_Blue_ID = (2, 24, 81)
        self.Light_Blue_ID = (0, 0, 255)
        self.Square_Size = 180
        self.Mini_Game_Simon_Says_Object = SimonSays()
        self.Board = {}
        self.Color = {}
        self.Color_By_Index = {}
        self.Stack_Previous_Colours = []
        self.Stack_Size = 0
        self.Current_Index_In_Stack = 0

    def Init_Game(self):
        pygame.init()
        self.Screen = pygame.display.set_mode(self.Window_Size)
        pygame.display.set_caption("Simon says")
        self.Set_Background()

    def Set_Background(self):
        self.Screen.fill(self.Grey_ID)

    def Refresh_Background(self):
        pygame.display.flip()

    def Display_New_Board(self):
        pass

    def Place_Piece(self,X_Coordinate,Y_Coordinate,Image):
        Image = pygame.image.load(Image)
        self.Screen.blit(Image, (X_Coordinate,Y_Coordinate))

    def Draw_Squares(self):
        pygame.draw.rect(self.Screen, self.Dark_Green_ID,
                         [ 110,
                          100,
                          self.Square_Size,
                          self.Square_Size])

        pygame.draw.rect(self.Screen, self.Dark_Red_ID,
                         [290,
                          100,
                          self.Square_Size,
                          self.Square_Size])

        pygame.draw.rect(self.Screen, self.Dark_Yellow_ID,
                         [110,
                          280,
                          self.Square_Size,
                          self.Square_Size])

        pygame.draw.rect(self.Screen, self.Dark_Blue_ID,
                         [290,
                          280,
                          self.Square_Size,
                          self.Square_Size])
        self.Refresh_Background()

    def Animate_Selected_Square(self,color_type):
        if color_type == "dark-green":
          pygame.draw.rect(self.Screen, self.Light_Green_ID,
                         [110,
                          100,
                          self.Square_Size,
                          self.Square_Size])

          pygame.display.flip()
          time.sleep(0.8)

          pygame.draw.rect(self.Screen, self.Dark_Green_ID,
                           [110,
                            100,
                            self.Square_Size,
                            self.Square_Size])

          pygame.display.flip()
          time.sleep(0.5)



        elif color_type == "dark-red":
          pygame.draw.rect(self.Screen, self.Light_Red_ID,
                         [290,
                          100,
                          self.Square_Size,
                          self.Square_Size])

          pygame.display.flip()
          time.sleep(0.8)

          pygame.draw.rect(self.Screen, self.Dark_Red_ID,
                           [290,
                            100,
                            self.Square_Size,
                            self.Square_Size])

          pygame.display.flip()
          time.sleep(0.5)

        elif color_type == "dark-blue":
          pygame.draw.rect(self.Screen, self.Light_Blue_ID,
                         [290,
                          280,
                          self.Square_Size,
                          self.Square_Size])

          pygame.display.flip()
          time.sleep(0.8)

          pygame.draw.rect(self.Screen, self.Dark_Blue_ID,
                           [290,
                            280,
                            self.Square_Size,
                            self.Square_Size])

          pygame.display.flip()
          time.sleep(0.5)



        elif color_type == "dark-yellow":
          pygame.draw.rect(self.Screen, self.Light_Yellow_ID,
                         [110,
                          280,
                          self.Square_Size,
                          self.Square_Size])

          pygame.display.flip()
          time.sleep(0.8)

          pygame.draw.rect(self.Screen, self.Dark_Yellow_ID,
                           [110,
                            280,
                            self.Square_Size,
                            self.Square_Size])

          pygame.display.flip()
          time.sleep(0.5)


    def Get_Random_Colour(self):
        Random_Colour_Index = random.randint(0,3)
        return self.Color_By_Index[Random_Colour_Index]

    def Show_Previous_Moves(self):
        self.Stack_Size += 1
        self.Stack_Previous_Colours.append(self.Get_Random_Colour())

        for previous in self.Stack_Previous_Colours:
            self.Animate_Selected_Square(previous)

    def Steps_Into_Game(self):
        return len(self.Stack_Previous_Colours)

    def Display_Start_Button(self):
        self.Place_Piece(680,480,"start-button.png")
        self.Refresh_Background()
        time.sleep(1)

    def Clicked_On_Start_Button(self,Coordinates_List):
        X_Coordinates = Coordinates_List[0]
        Y_Coordinates = Coordinates_List[1]
        if X_Coordinates >= 682 and X_Coordinates <= 743 and Y_Coordinates >= 483 and Y_Coordinates <= 542:
            return 1
        return 0

    def Valid_Current_Move(self,Element_To_Check):
        if Element_To_Check== self.Stack_Previous_Colours[self.Current_Index_In_Stack]:
            return 1
        return 0

    def Update_Index_In_Stack(self):
        self.Current_Index_In_Stack +=1


    def Get_Position_On_Board_By_Click_Coordinates(self,Click_Coordinates):
        X_Coordinate = Click_Coordinates[0]
        Y_Coordinate = Click_Coordinates[1]

        if X_Coordinate >= 110 and X_Coordinate <= 290 and Y_Coordinate >= 100 and Y_Coordinate <= 280:
            return [0,0]
        elif X_Coordinate >= 291 and X_Coordinate <= 471 and Y_Coordinate >= 101 and Y_Coordinate <= 280:
                return [0,1]
        elif X_Coordinate >= 111 and X_Coordinate <= 290 and Y_Coordinate >= 281 and Y_Coordinate <= 460:
                return [1,0]
        elif X_Coordinate >= 291 and X_Coordinate <= 470 and Y_Coordinate >= 281 and Y_Coordinate <= 460:
                return [1,1]
        return None

    def In_Board(self,X_Coordinates,Y_Coordinates):
        if X_Coordinates >= 110 and X_Coordinates <= 470 and Y_Coordinates >= 100 and Y_Coordinates <= 460:
            return 1
        return 0

    def Wait(self):
        time.sleep(0.8)

    def Update_Stack_Size(self):
        self.Stack_Size +=1

    def Check_End_Group(self):
        if self.Current_Index_In_Stack == self.Stack_Size:
          return 1
        return 0

    def Reset_Index_Stack(self):
        self.Current_Index_In_Stack = 0

    def Init_Simon_Says(self):
        self.Init_Game()
        self.Draw_Squares()
        self.Place_Piece(35,30,"empty-square.png")
        self.Board = self.Mini_Game_Simon_Says_Object.Generate_Board()
        self.Color["dark-blue"] = self.Light_Blue_ID
        self.Color["dark-yellow"] = self.Light_Yellow_ID
        self.Color["dark-green"] = self.Light_Green_ID
        self.Color["dark-red"] = self.Light_Red_ID
        self.Color_By_Index[0] = "dark-green"
        self.Color_By_Index[1] = "dark-red"
        self.Color_By_Index[2] = "dark-yellow"
        self.Color_By_Index[3] = "dark-blue"

        pygame.display.flip()


    def Run_Main(self):
        self.Init_Simon_Says()
        self.Display_Start_Button()
        stop_click = 1
        firstMove = 0
        Started_Game = 0
        while stop_click:
            for click in pygame.event.get():
                if click.type == pygame.MOUSEBUTTONDOWN:
                    click_coordinates = pygame.mouse.get_pos()
                    X_Coordinates = click_coordinates[0]
                    Y_Coordinates = click_coordinates[1]

                    if self.Clicked_On_Start_Button(click_coordinates) and Started_Game == 0:
                        Started_Game = 1
                        self.Wait()
                        self.Show_Previous_Moves()



                    elif self.Get_Position_On_Board_By_Click_Coordinates(click_coordinates) != None:

                        self.Current_Index_In_Stack = 0
                        Matrix_Row = self.Get_Position_On_Board_By_Click_Coordinates(click_coordinates)[0]
                        Matrix_Column = self.Get_Position_On_Board_By_Click_Coordinates(click_coordinates)[1]


                        if self.Valid_Current_Move(self.Board[Matrix_Row][Matrix_Column]):
                          print("VLAD")
                          self.Show_Previous_Moves()
                          Stop_Remember_Path = 1
                          self.Stack_Size = 1

                          while Stop_Remember_Path:
                            for next_click in pygame.event.get():
                                if next_click.type == pygame.MOUSEBUTTONDOWN:
                                    second_click_coordinates = pygame.mouse.get_pos()
                                    if self.Get_Position_On_Board_By_Click_Coordinates(second_click_coordinates) != None:
                                        print("*")
                                        Matrix_Row = self.Get_Position_On_Board_By_Click_Coordinates(second_click_coordinates)[0]
                                        Matrix_Column = self.Get_Position_On_Board_By_Click_Coordinates(second_click_coordinates)[1]
                                        if self.Valid_Current_Move(self.Board[Matrix_Row][Matrix_Column]):
                                            print(self.Stack_Size,self.Current_Index_In_Stack)
                                            if self.Check_End_Group():
                                              self.Reset_Index_Stack()
                                              #self.Update_Stack_Size()
                                              self.Wait()
                                              self.Show_Previous_Moves()
                                            else:
                                              #print("GOOD")
                                              self.Update_Index_In_Stack()
                                        else:
                                            Stop_Remember_Path = 0
                                            print("POC")
                                            break


                    else:
                        print("BAD")







test = simon_says_GUI()
test.Run_Main()


