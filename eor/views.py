import json

from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def articleone(request):
    return render(request, "article/articleone.html")

def articletwo(request):
    return render(request, "article/articletwo.html")

def articlethree(request):
    return render(request, "article/articlethree.html")

def articlefour(request):
    return render(request, "article/articlefour.html")


def mobility_ratio(request):

    result = None
    interpretation = None

    if request.method == "POST":

        krw = float(request.POST.get("krw"))
        kro = float(request.POST.get("kro"))
        muw = float(request.POST.get("muw"))
        muo = float(request.POST.get("muo"))

        # Mobility Ratio Formula
        result = (krw / muw) / (kro / muo)

        # Engineering interpretation
        if result < 1:
            interpretation = "Stable displacement (Good sweep efficiency)"
        elif result == 1:
            interpretation = "Neutral displacement"
        else:
            interpretation = "Unstable displacement (Fingering likely)"

    return render(request, "mobility_ratio.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render

def areal_sweep(request):

    result = None
    interpretation = None

    if request.method == "POST":

        As = float(request.POST.get("As"))
        At = float(request.POST.get("At"))

        result = (As / At) * 100

        if result < 50:
            interpretation = "Poor sweep efficiency (high bypassed oil risk)"
        elif result <= 75:
            interpretation = "Moderate sweep efficiency"
        else:
            interpretation = "Good sweep efficiency (efficient displacement)"

    return render(request, "areal_sweep.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render

def volumetric_sweep(request):

    result = None
    interpretation = None

    if request.method == "POST":

        EA = float(request.POST.get("EA"))
        ED = float(request.POST.get("ED"))
        EI = float(request.POST.get("EI"))

        result = EA * ED * EI

        if result < 0.4:
            interpretation = "Poor volumetric sweep (low reservoir contact)"
        elif result <= 0.7:
            interpretation = "Moderate volumetric sweep"
        else:
            interpretation = "Good volumetric sweep efficiency"

    return render(request, "volumetric_sweep.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def breakthrough_time(request):

    result = None
    interpretation = None
    production_data = []

    if request.method == "POST":

        phi = float(request.POST.get("phi"))
        A = float(request.POST.get("A"))
        h = float(request.POST.get("h"))
        swi = float(request.POST.get("swi"))
        qw = float(request.POST.get("qw"))
        Bw = float(request.POST.get("Bw"))

        result = (phi * A * h * swi) / (qw * Bw)

        if result < 500:
            interpretation = "Early breakthrough (poor sweep efficiency)"
        elif result <= 1500:
            interpretation = "Moderate breakthrough behavior"
        else:
            interpretation = "Delayed breakthrough (good reservoir performance)"

        # Simulated production decline curve
        base_rate = 1000

        for t in range(0, 10):
            oil_rate = base_rate * (0.88 ** t)

            production_data.append({
                "time": t,
                "oil_rate": oil_rate
            })

    return render(request, "breakthrough_time.html", {
        "result": result,
        "interpretation": interpretation,
        "production_data": production_data
    })


from django.shortcuts import render

def recovery_factor(request):

    result = None
    interpretation = None

    if request.method == "POST":

        Np = float(request.POST.get("Np"))
        N = float(request.POST.get("N"))

        result = (Np / N) * 100

        if result < 20:
            interpretation = "Poor recovery (primary depletion stage)"
        elif result <= 40:
            interpretation = "Moderate recovery (waterflood stage)"
        else:
            interpretation = "Good recovery (EOR likely applied)"

    return render(request, "recovery_factor.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def mmp(request):

    result = None
    interpretation = None

    if request.method == "POST":

        T = float(request.POST.get("T"))
        API = float(request.POST.get("API"))

        # empirical constants (typical simplified values)
        a = 150
        b = 0.8
        c = 3.5

        result = a + (b * T) + (c * API)

        if result < 1500:
            interpretation = "Low MMP → Favorable for CO₂ injection"
        elif result <= 3000:
            interpretation = "Moderate MMP → Requires optimized injection design"
        else:
            interpretation = "High MMP → CO₂ flooding less economical"

    return render(request, "mmp.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def fractional_flow(request):

    result = None
    interpretation = None

    if request.method == "POST":

        krw = float(request.POST.get("krw"))
        kro = float(request.POST.get("kro"))
        muw = float(request.POST.get("muw"))
        muo = float(request.POST.get("muo"))

        result = 1 / (1 + (kro * muw) / (krw * muo))

        if result < 0.3:
            interpretation = "Oil-dominated flow regime"
        elif result <= 0.7:
            interpretation = "Transition zone (efficient displacement developing)"
        else:
            interpretation = "Water-dominated flow (possible breakthrough)"

    return render(request, "fractional_flow.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def ooip(request):

    result = None

    if request.method == "POST":

        A = float(request.POST.get("A"))
        h = float(request.POST.get("h"))
        phi = float(request.POST.get("phi"))
        Sw = float(request.POST.get("Sw"))
        Bo = float(request.POST.get("Bo"))

        result = (7758 * A * h * phi * (1 - Sw)) / Bo

    return render(request, "ooip.html", {
        "result": result
    })


from django.shortcuts import render

def edbt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        Sor = float(request.POST.get("Sor"))
        Sob = float(request.POST.get("Sob"))
        Swi = float(request.POST.get("Swi"))

        result = (Sor - Sob) / (Sor - Swi)

        if result < 0.3:
            interpretation = "Poor displacement efficiency at breakthrough"
        elif result <= 0.6:
            interpretation = "Moderate displacement efficiency"
        else:
            interpretation = "Good displacement efficiency"

    return render(request, "edbt.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render
import math

def eabt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        M = float(request.POST.get("M"))

        result = 0.55 + (0.032 / M) + (0.032 / math.exp(M)) - (0.005 * M)

        if M < 1:
            interpretation = "Favorable displacement (stable flood front)"
        elif M <= 2:
            interpretation = "Moderate sweep efficiency"
        else:
            interpretation = "Unfavorable mobility ratio (fingering likely)"

    return render(request, "eabt.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render

def tbt(request):

    result = None
    interpretation = None
    selected_model = None

    if request.method == "POST":

        selected_model = request.POST.get("model")
        Iw = float(request.POST.get("Iw"))
        Qibt = float(request.POST.get("Qibt"))

        # Formula 1
        if selected_model == "pv":

            PV = float(request.POST.get("PV"))
            result = (PV * Qibt) / Iw

        # Formula 2
        elif selected_model == "geo":

            phi = float(request.POST.get("phi"))
            A = float(request.POST.get("A"))
            L = float(request.POST.get("L"))

            result = (phi * A * L * Qibt) / Iw

        # Interpretation
        if result < 500:
            interpretation = "Early breakthrough (poor sweep efficiency)"
        elif result <= 1500:
            interpretation = "Moderate breakthrough timing"
        else:
            interpretation = "Delayed breakthrough (efficient displacement)"

    return render(request, "tbt.html", {
        "result": result,
        "interpretation": interpretation,
        "selected_model": selected_model
    })


from django.shortcuts import render

def npbt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        N = float(request.POST.get("N"))
        Eabt = float(request.POST.get("Eabt"))
        Edbt = float(request.POST.get("Edbt"))

        result = N * Eabt * Edbt

        if result < 10000:
            interpretation = "Low oil production at breakthrough (inefficient flood)"
        elif result <= 50000:
            interpretation = "Moderate oil production at breakthrough"
        else:
            interpretation = "High recovery efficiency at breakthrough"

    return render(request, "npbt.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def wibt(request):

    result = None
    interpretation = None
    selected_model = None

    if request.method == "POST":

        selected_model = request.POST.get("model")

        PV = float(request.POST.get("PV"))

        # Model 1: saturation-based
        if selected_model == "sat":

            Swf = float(request.POST.get("Swf"))
            Swi = float(request.POST.get("Swi"))

            result = PV * (Swf - Swi)

        # Model 2: injection-based
        elif selected_model == "inj":

            Qibt = float(request.POST.get("Qibt"))

            result = PV * Qibt

        # Interpretation
        if result < 10000:
            interpretation = "Low water volume at breakthrough"
        elif result <= 50000:
            interpretation = "Moderate water injection behavior"
        else:
            interpretation = "High water injection (strong flood support)"

    return render(request, "wibt.html", {
        "result": result,
        "interpretation": interpretation,
        "selected_model": selected_model
    })


from django.shortcuts import render

def qibt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        model = request.POST.get("model")

        # Model 1: derivative-based
        if model == "dfw":

            dfw_dsw = float(request.POST.get("dfw_dsw"))

            result = 1 / dfw_dsw

        # Model 2: saturation difference
        elif model == "sat":

            Swf = float(request.POST.get("Swf"))
            Swi = float(request.POST.get("Swi"))

            result = Swf - Swi

        # Interpretation
        if result < 0.2:
            interpretation = "Low injection response"
        elif result <= 0.5:
            interpretation = "Moderate injection behavior"
        else:
            interpretation = "High injection efficiency / strong flood front"

    return render(request, "qibt.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def pv(request):

    result = None
    interpretation = None

    if request.method == "POST":

        phi = float(request.POST.get("phi"))
        A = float(request.POST.get("A"))
        L = float(request.POST.get("L"))

        result = (phi * A * L) / 5.615

        if result < 10000:
            interpretation = "Small reservoir pore volume"
        elif result <= 50000:
            interpretation = "Moderate reservoir size"
        else:
            interpretation = "Large reservoir system"

    return render(request, "pv.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def ns(request):

    result = None
    interpretation = None

    if request.method == "POST":

        model = request.POST.get("model")

        Bo = float(request.POST.get("Bo"))

        # Model 1: PV-based
        if model == "pv":

            PV = float(request.POST.get("PV"))
            Soi = float(request.POST.get("Soi"))

            result = (PV * Soi) / Bo

        # Model 2: volumetric
        elif model == "vol":

            A = float(request.POST.get("A"))
            h = float(request.POST.get("h"))
            phi = float(request.POST.get("phi"))
            Swi = float(request.POST.get("Swi"))

            result = (7758 * A * h * phi * (1 - Swi)) / Bo

        # Interpretation
        if result < 1e5:
            interpretation = "Low hydrocarbon in place"
        elif result <= 5e5:
            interpretation = "Moderate hydrocarbon volume"
        else:
            interpretation = "Large reservoir hydrocarbon accumulation"

    return render(request, "ns.html", {
        "result": result,
        "interpretation": interpretation
    })


# Graph part

import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
import json

def relperm_plot(request):

    plot_url = None

    if request.method == "POST":

        sw_values = []
        kr_ratio_values = []

        # collect 15 values
        for i in range(1, 16):

            sw = request.POST.get(f"sw{i}")
            kr = request.POST.get(f"kr{i}")

            if sw and kr:
                sw_values.append(float(sw))
                kr_ratio_values.append(float(kr))

        # sort for proper plotting
        sorted_data = sorted(zip(sw_values, kr_ratio_values))
        sw_values, kr_ratio_values = zip(*sorted_data)

        # plotting
        plt.figure()
        plt.plot(sw_values, kr_ratio_values, marker='o', label="Kro/Krw vs Sw")

        plt.xlabel("Water Saturation (Sw)")
        plt.ylabel("Relative Permeability Ratio (Kro/Krw)")
        plt.title("Relative Permeability Curve")

        plt.grid(True)
        plt.legend()

        # auto scale
        plt.autoscale()

        # save image to memory
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        image_png = buffer.getvalue()
        buffer.close()

        plot_url = base64.b64encode(image_png).decode('utf-8')

        plt.close()

    return render(request, "relperm_plot.html", {
        "plot_url": plot_url
    })


from django.shortcuts import render

def fw_plot(request):

    plot_data = None

    if request.method == "POST":

        sw_values = []
        fw_values = []

        # collect 15 inputs
        for i in range(1, 16):

            sw = request.POST.get(f"sw{i}")
            fw = request.POST.get(f"fw{i}")

            if sw and fw:
                sw_values.append(float(sw))
                fw_values.append(float(fw))

        # sort for proper curve
        sorted_data = sorted(zip(sw_values, fw_values))
        sw_values, fw_values = zip(*sorted_data)

        # build chart data for frontend widget
        data = []
        for i in range(len(sw_values)):
            data.append({
                "Sw": sw_values[i],
                "Fw": fw_values[i]
            })

        plot_data = data

    return render(request, "fw_plot.html", {
        "plot_data": json.dumps(plot_data)
    })


from django.shortcuts import render

from django.shortcuts import render

def fw_dual_plot(request):

    plot_data = []

    if request.method == "POST":

        sw_values = []
        fw_values = []
        dfw_values = []

        for i in range(1, 16):

            sw = request.POST.get(f"sw{i}")
            fw = request.POST.get(f"fw{i}")
            dfw = request.POST.get(f"dfw{i}")

            if sw and fw and dfw:
                sw_values.append(float(sw))
                fw_values.append(float(fw))
                dfw_values.append(float(dfw))

        if len(sw_values) >= 2:

            combined = sorted(zip(sw_values, fw_values, dfw_values))
            sw_values, fw_values, dfw_values = zip(*combined)

            plot_data = [
                {
                    "Sw": float(sw_values[i]),
                    "Fw": float(fw_values[i]),
                    "dfw_dSw": float(dfw_values[i])
                }
                for i in range(len(sw_values))
            ]

    return render(request, "fw_dual.html", {
        "plot_data": json.dumps(plot_data)   # ✔ RAW PYTHON LIST (IMPORTANT)
    })



from django.shortcuts import render
import math

def slope(request):

    result = None
    interpretation = None

    if request.method == "POST":

        kro1 = float(request.POST.get("kro1"))
        krw1 = float(request.POST.get("krw1"))
        kro2 = float(request.POST.get("kro2"))
        krw2 = float(request.POST.get("krw2"))

        Sw1 = float(request.POST.get("Sw1"))
        Sw2 = float(request.POST.get("Sw2"))

        term1 = math.log(kro2 / krw2)
        term2 = math.log(kro1 / krw1)

        result = (term1 - term2) / (Sw2 - Sw1)

        if abs(result) < 1:
            interpretation = "Stable displacement (smooth fractional flow curve)"
        elif abs(result) <= 3:
            interpretation = "Moderate mobility variation"
        else:
            interpretation = "Unstable displacement (high fingering tendency)"

    return render(request, "slope.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render
from pint import UnitRegistry

ureg = UnitRegistry()

def unit_converter(request):

    result = None
    error = None

    if request.method == "POST":

        try:

            value = float(request.POST.get("value"))

            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")

            quantity = ureg.Quantity(value, from_unit)

            converted = quantity.to(to_unit)

            result = round(converted.magnitude, 6)

        except Exception as e:
            error = str(e)

    return render(request, "unit-converter.html", {
        "result": result,
        "error": error
    })
