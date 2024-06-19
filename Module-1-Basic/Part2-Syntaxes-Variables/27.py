
# T-1 yanvar N-hafta kunidan
 # boshlanadi (N€[1;7]), hafta kunlari quyidagicha nomerlangan bo’lsa;
 # 1-dushanba, 2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba, 7-yakshanba bo`lsa, berilgan K (1-365) butun sonini yilning kuni deb hisoblab  u haftaning qaysi kuniga to`g`ri kelishi aniqlansin


n = int(input("Yil kunini kiriting = "))
day_of_week = ((n-2)) % 7
print(day_of_week)