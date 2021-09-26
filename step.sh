
echo "Configuring the bot"
if [[ $CLIENT == "Both" ]]
then
   git clone https://github.com/TeamSpeedo/Speedo.git
   cd Speedo
   python3 -m Speedo
   python3 -m main_start
elif [[ $CLIENT == "Tele" ]]
then
   git clone https://github.com/TeamSpeedo/Speedo.git
   cd Speedo
   python3 -m Speedo
else
   git clone https://github.com/TeamSpeedo/Speedo
   cd Speedo
   python3 -m main_start
fi
