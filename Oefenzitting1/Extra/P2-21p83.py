y = int(input("Year: "))

mod_a_19_y = y % 19

mod_c_100_y = y % 100
quotient_b_100_y = y // 100

quotient_d = quotient_b_100_y // 4
mod_e = quotient_b_100_y % 4

quotient_g = (8 * quotient_b_100_y + 13) // 25

mod_h = ((19 * mod_a_19_y) + quotient_b_100_y - quotient_d - quotient_g + 15) % 30

quotient_j = mod_c_100_y // 4
remainder_k = mod_c_100_y % 4

quotient_m = (mod_a_19_y + (11 * mod_h)) // 319

#step 9
mod_r = ((2*mod_e) + (2 * quotient_j) - remainder_k - mod_h + quotient_m + 32) % 7

#step 10
quotient_n = (mod_h - quotient_m + mod_r + 90) // 25

#step 11
mod_p = (mod_h - quotient_m + mod_r + quotient_n +19) % 32

print("Eastern falls on day %i in month %i" % (mod_p,quotient_n))
print("%i/%i/%i" % (mod_p,quotient_n,y))