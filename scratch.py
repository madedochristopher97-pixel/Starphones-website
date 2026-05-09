import re

data = """
Infinix|X6880 256+8|Hot 50 Pro|27,200|5,440|206|164|142|8,704|183|145|127
Infinix|X6880 128+8|Hot 50 Pro|26,600|5,320|201|160|139|8,512|179|142|124
Infinix|X6855 256+8|note 50 Pro 4G|34,900|6,980|264|210|182|11,168|224|179|155
Infinix|X6725 64+3|Smart 10 4G|12,000|2,400|100|83|73|3,840|85|70|62
Infinix|X6725 128+4|Smart 10 4G|14,000|2,800|111|88|77|4,480|99|82|72
Infinix|X6728B 128+6|Hot 60i|17,000|3,400|134|107|93|5,440|114|91|79
Infinix|X6728 256+8|Hot 60i|20,000|4,000|158|125|109|6,400|134|107|93
Infinix|X6886 128+8|Hot 60 Pro+|26,600|5,320|201|160|139|8,512|179|142|124
Infinix|X6886 256+8|Hot 60 Pro+|30,500|6,100|231|184|159|9,760|196|156|135
Infinix|X6725 64+4|Smart 10 4G|12,600|2,520|100|79|69|4,032|90|74|65
Infinix|X6728B 128+4|Hot 60i|14,850|2,970|117|93|81|4,752|100|79|69
Infinix|X6525D 64+2|Smart 10HD|10,000|2,000|84|69|61|3,200|71|59|52
Infinix|X6887 256+8|Note Edge|36,200|7,240|274|218|189|11,584|233|185|160
Infinix|X6878 256+8|Note 60 Pro|44,000|8,800|326|257|218|14,080|283|225|195
Infinix|X6840 128+4|Smart 20|15,000|3,000|119|94|82|4,800|101|80|70
Infinix|X6840 64+4|Smart 20|13,200|2,640|104|83|72|4,224|94|77|68
Infinix|X1102B 128+4|XPAD 30E|19,000|3,800|150|119|104|6,080|128|101|88
Itel|A6610L 128+4|A90|10,700|2,140|89|74|65|3,424|76|63|55
Itel|C671L 128+6|City 100|12,700|2,540|100|80|70|4,064|90|74|66
Itel|C671L 256+4|City 100|12,900|2,580|102|81|71|4,128|92|76|67
Itel|S688LN 256+8|S26 Ultra 8|26,500|5,300|200|160|138|8,480|178|141|123
Itel|A6611L 64+2|A100C|11,000|2,200|92|76|67|3,520|78|64|57
Itel|a669w 2+64|A06|8,900|1,780|74|61|54|2,848|63|52|46
Itel|C681l 128+4|City 200|15,500|3,100|122|97|85|4,960|104|83|72
Itel|A675L 128+3|A200|13,500|2,700|107|85|74|4,320|96|79|70
Oppo|CPH2781 256+8|A6 Pro 5G|42,000|8,400|311|246|208|13,440|270|215|186
Oppo|CPH2799 256+8|A6 Pro 4G|37,800|7,560|280|221|188|12,096|243|194|168
Oppo|CPH2727 128+6|A5|26,000|5,200|197|157|136|8,320|175|139|121
Oppo|CPH2727 256+8|A5|28,200|5,640|213|170|147|9,024|189|150|131
Oppo|CPH2819 128+4|A6X|19,300|3,860|152|121|106|6,176|130|103|90
Oppo|CPH2819 256+4|A6X|24,000|4,800|190|150|131|7,680|161|128|112
Oppo|CPH2641 64+4|A3X|15,200|3,040|120|95|83|4,864|102|81|71
Oppo|CPH2641 128+4|A3X|19,500|3,900|154|122|107|6,240|131|104|91
Oppo|CPH2819 64+4|A6X|14,800|2,960|117|93|81|4,736|99|79|69
Tecno|CM6 256+8|Camon 40 Pro|38,800|7,760|287|227|192|12,416|249|199|172
Tecno|CLA5 128+6|camon 30S|27,500|5,500|208|166|143|8,800|185|147|128
Tecno|KM5 128+4|Spark 40|16,000|3,200|126|100|88|5,120|107|85|74
Tecno|KM4 64+3|Pop 10|13,000|2,600|103|81|71|4,160|92|76|67
Tecno|KM6 128+8|SPARK 40 Pro|21,750|4,350|172|136|119|6,960|146|116|101
Tecno|KM7 128+8|SPARK 40 Pro+|27,500|5,500|208|166|143|8,800|185|147|128
Tecno|KM7 256+8|SPARK 40|30,000|6,000|227|181|156|9,600|193|154|133
Tecno|KM5 256+8|Pro+ Spark 40|18,900|3,780|149|118|103|6,048|127|101|88
Tecno|KM4K 128+4|Pop 10 Pro|14,000|2,800|111|88|77|4,480|99|82|72
Tecno|KM7k 256+8|Spark Slim|30,500|6,100|231|184|159|9,760|196|156|135
Tecno|T1102 128+4|Megapad|20,500|4,100|162|129|112|6,560|138|109|95
Tecno|T1102 256+8|Megapad|24,400|4,880|193|153|134|7,808|164|130|114
Tecno|KN3 64+4|Pop 20|14,250|2,850|113|89|78|4,560|101|84|74
Tecno|KN3 128+4|Pop 20|16,800|3,360|133|105|92|5,376|113|90|78
Tecno|CN5 256+8|Camon 50|38,500|7,700|285|225|191|12,320|248|197|171
Tecno|CN5C 256+8|Camon 50|41,900|8,380|310|245|208|13,408|269|215|186
Tecno|KN4 128+4|Pro Spark 50|17,500|3,500|138|110|96|5,600|118|93|81
Tecno|KN4 256+4|Spark 50|20,200|4,040|160|127|111|6,464|136|108|94
"""

html_rows = []
for line in data.strip().split('\n'):
    cols = line.split('|')
    brand = f'<td class="brand-cell">{cols[0]}</td>'
    cells = [f'<td>{c}</td>' for c in cols[1:]]
    html_rows.append(f'                            <tr>{brand}{"".join(cells)}</tr>')

table_html = f"""
        <!-- Pricing Table Section -->
        <section class="content-section" style="background-color: var(--color-white);">
            <div class="container">
                <div class="text-block text-center animate-on-scroll" style="margin-bottom: var(--space-6);">
                    <h2 class="section-title">Full Device Catalog & Pricing</h2>
                    <p class="section-subtitle">Comprehensive list of all models and Lipa Mdogo Mdogo plans (15% and 30% Deposits).</p>
                </div>
                
                <div class="pricing-table-container animate-on-scroll">
                    <table class="pricing-table">
                        <thead>
                            <tr>
                                <th>Brand</th>
                                <th>Model</th>
                                <th>Name</th>
                                <th>RRP (KES)</th>
                                <th>Std. Deposit</th>
                                <th>Daily (6M)</th>
                                <th>Daily (9M)</th>
                                <th>Daily (12M)</th>
                                <th>VIP Deposit</th>
                                <th>VIP (6M)</th>
                                <th>VIP (9M)</th>
                                <th>VIP (12M)</th>
                            </tr>
                        </thead>
                        <tbody>
{chr(10).join(html_rows)}
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
"""

with open('phones.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = "                </div>\n            </div>\n        </section>\n    </main>"
replacement = f"                </div>\n            </div>\n        </section>\n{table_html}    </main>"

new_content = content.replace(target, replacement)

with open('phones.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Table inserted successfully")
