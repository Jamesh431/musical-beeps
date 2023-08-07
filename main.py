# import os
# import sys
# import argparse
# import musicalbeeps


# def PlayNote(Note, Octive, Accidental, Duration, Volume):
#     # Accidental is either # (sharp) or b (flat) or '' (none)
#     global TempPlayer
#     TempPlayer = musicalbeeps.Player(volume=float(Volume), mute_output=False)
#     TempPlayer.play_note("{}{}{}".format(Note, Octive, Accidental), Duration)
#     TempPlayer = None


# player = (1, False)


# def player_loop(args, input_file):
#     notes_player = musicalbeeps.Player(args.volume, args.silent)

#     for line in input_file:
#         valid_duration = True
#         line = line.rstrip()
#         if len(line) > 0:
#             try:
#                 note, duration_str = line.split(":")
#             except:
#                 note, duration_str = line, ".5"
#             try:
#                 duration = float(duration_str)
#             except:
#                 valid_duration = False
#                 print(
#                     "Error: invalid duration: '" + duration_str + "'", file=sys.stderr
#                 )
#             if valid_duration:
#                 notes_player.play_note(note, duration)


# player_loop()
# # print("Running...")
# # PlayNote("B", 4, "#", 5, 1)
# # print("Done!")


# # with open("stftk.txt") as music:
# #     musicalbeeps.layer.play_note(music)
# # musicalbeeps.beepsplayer

# musicalbeeps.Player()

# player_loop(player, "stftk.txt")
# """
# D D C A D C F# D C# D C# A D C# F# D B D B F# D B G D A E A F# G F# E D
# """
# # e|-----------------|-----------------|-----------------|-----------------|
# # B|-----------------|-----------------|-----------------|-----------------|
# # G|-----------------|-----------------|-----------------|-----------------| x2
# # D|---0---7-0---4-0-|---0---7-0---4-0-|---0---4-0---5-0-|---2---4-5-4-2-0-|
# # A|-5---5-----5-----|-4---4-----4-----|-2---2-----2-----|-0---0-----------|
# # E|-----------------|-----------------|-----------------|-----------------


def f(s):
    p, r = ("-", "")
    if len(s) < 10:
        return "___"
    if len(s) == 10:
        r = "1"
    return f"{r}({s[0:3]}) {s[3:6]}{p}{s[6:10]}"


print(f("8080808080"))
