def effect_protect(final_product_price, final_rate, raw_material_price, raw_rate):
    # 国内附加值=进口价格*(1+关税)-原材料价格*(1+关税)
    domestic_growth = (1 + final_rate) * final_product_price - (1 + raw_rate) * raw_material_price
    foreign_growth = final_product_price - raw_material_price

    protect_rate = (domestic_growth - foreign_growth) / foreign_growth
    print("{:.2f}%".format(protect_rate * 100))
