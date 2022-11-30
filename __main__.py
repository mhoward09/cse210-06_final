from constants import * #imports all variables, classes, and functions from the constants file
from space_invaders.game.directing.director import Director #imports the Director class from the director file which is the main game-loop that runs and controls the game
from space_invaders.game.directing.scene_manager import SceneManager #imports the SceneManager class from the scene_manager file that is resposible ofr rendering/building each level to the video service and game window


def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()