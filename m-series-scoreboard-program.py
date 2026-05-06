# ==== Program Utama Kelompok (DONE) ====

Turnamen = []
Turnamen.append([{"Oura": [86, 859224, 79]}, {"Jess": [90, 891321, 82]}, {"Donkey": [66, 567921, 74]}, {"Wann": [89, 891454, 78]}, {"Rekt": [48, 4847921, 77]}])
Turnamen.append([{"Lemon": [79, 746515, 61]}, {"Tuturu": [91, 891321, 80]}, {"R7": [69, 522742, 74]}, {"Tuturu": [91, 904846, 77]}, {"LJ": [66, 567921, 74]}])
Turnamen.append([{"Nino": [75, 746413, 75]}, {"Hijume": [78, 813546, 78]}, {"Arfy": [77, 756221, 78]}, {"Rey": [60, 468751, 74]}, {"Alek": [77, 679154, 78]}])

label = ["Team Evos Legend", "Team RRQ", "Team Alter Ego"]

print("Welcome to M Series!\n")
nama = input("Siapa nama mu: ")

print("Hi,",nama,"! Silahkan cek tim kami!\n")

def timturnamen(a):
  print("\n============================= Scoreboard M Series 2026 =============================")
  for i, tim in enumerate(Turnamen):
    print(label[i])

    for data in tim:
        nama_player             = list(data.keys())[0]
        kills, damage, winrate  = list(data.values())[0]

        skor = kills + (damage // 100) + winrate

        if skor >= 8500:
            grade = "Immortal"
        elif skor >= 7000:
            grade = "Glory"
        else:
            grade = "Honor"

        print(nama_player, "\t| Kills:", kills,"\t DMG:", damage, "\tWR:", winrate, "% \t| Skor:", skor, "\t →", grade)

    print()
timturnamen(Turnamen)

while True:
  nextstep = input("\nApakah anda ingin update data? (Tambah/Hapus/Berhenti): ")
  if nextstep == "Tambah":
    namaplayer = input("Masukkan nama pemain: ")
    kill = int(input("Masukkan jumlah kill: "))
    damage = int(input("Masukkan jumlah damage: "))
    winrate = int(input("Masukkan jumlah winrate: "))
    data = {namaplayer: [kill, damage, winrate]}
    tim = input("Masukkan nama tim: ")
    if tim not in label:
      Turnamen.append([data])
      label.append(tim)
    else:
      findteam = label.index(tim)
      if len(Turnamen[findteam]) >= 7:
          print("Maaf, tim sudah penuh (maksimal 7 pemain).")
          continue
      Turnamen[findteam].append(data)
    timturnamen(Turnamen)
  elif nextstep == "Hapus":
    namaplayer = input("Masukkan nama pemain: ")
    tim = input("Masukkan nama tim: ")
    if tim not in label:
      print("Tim tidak ditemukan.")
    else:
      find = label.index(tim)
      findplayer = False
      for i, player_data in enumerate(Turnamen[find]):
        if list(player_data.keys())[0] == namaplayer:
          Turnamen[find].pop(i)
          findplayer = True
          print('Pemain', namaplayer,'berhasil dihapus dari tim', tim)
           

      if not Turnamen[find]: 
        del Turnamen[find]  
        removedlabel = label.pop(find) 
        print('Tim', removedlabel, 'terhapus karena tidak memiliki pemain lagi.') 
        
      if not findplayer:
        print('Pemain',namaplayer,'tidak ditemukan di tim', tim)
      
      timturnamen(Turnamen)

  elif nextstep == "Berhenti":
    exit = True
    minim_member_teams = []
    for i in range(len(Turnamen)):
      jumlah_pemain = len(Turnamen[i])
      if jumlah_pemain < 5:
        exit = False
        minim_member_teams.append(label[i])
    
    if exit:
      print("Terima kasih sudah menggunakan aplikasi kami!")
      break
    else:
      print("\n===== PERINGATAN =====")
      print("Beberapa tim memiliki pemain di bawah batas minimum (5 orang):")
      for team_name in minim_member_teams:
        print(' -', team_name)
      print("Silahkan tambah pemain untuk tim-tim tersebut sebelum keluar.")
      timturnamen(Turnamen)

  else:
    print("Inputan tidak dimengerti!.")
    continue
