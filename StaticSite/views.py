from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Measurements
from .forms import SignUpForm
from imageLoader.models import DressesImages, ChaniyaCholiImages, HandWorkImages, BlouseImages
# Create your views here.


class TempMeasure:
    def __init__(self, value, bodypart, className):
        self.value = value
        self.bodypart = bodypart
        self.className = className


def addCustomer(request):
    measure = Measurements()

    M = []
    M.append(TempMeasure(measure.braSize, "bra size", "braSize"))
    M.append(TempMeasure(measure.height, "height", "height"))
    M.append(TempMeasure(measure.head, "head", "head"))
    M.append(TempMeasure(measure.neck, "neck", "neck"))
    M.append(TempMeasure(measure.upperBust, "upper Bust", "upperBust"))
    M.append(TempMeasure(measure.bust, "bust", "bust"))
    M.append(TempMeasure(measure.nippleToNipple,
                         "nipple To Nipple", "nippleToNipple"))
    M.append(TempMeasure(measure.nippleToShoulder,
                         "nipple To Shoulder", "nippleToShoulder"))
    M.append(TempMeasure(measure.underBust, "under Bust", "underBust"))
    M.append(TempMeasure(measure.waist, "waist", "waist"))
    M.append(TempMeasure(measure.highHip, "highHip", "highHip"))
    M.append(TempMeasure(measure.hip, "hip", "hip"))
    M.append(TempMeasure(measure.shoulderWidth,
                         "shoulder Width", "shoulderWidth"))
    M.append(TempMeasure(measure.bicep, "bicep", "bicep"))
    M.append(TempMeasure(measure.wrist, "wrist", "wrist"))
    M.append(TempMeasure(measure.insideArm, "insideArm", "insideArm"))
    M.append(TempMeasure(measure.aroundKnuckle,
                         "around Knuckle", "aroundKnuckle"))
    M.append(TempMeasure(measure.topOfThigh, "top Of Thigh", "topOfThigh"))
    M.append(TempMeasure(measure.insideLegToHeel,
                         "inside Leg To Heel", "insideLegToHeel"))
    M.append(TempMeasure(measure.aroundKnee, "around Knee", "aroundKnee"))
    M.append(TempMeasure(measure.aroundCalf, "around Calf", "aroundCalf"))
    M.append(TempMeasure(measure.aroundAnkle, "around Ankle", "aroundAnkle"))
    M.append(TempMeasure(measure.footWidth, "foot Width", "footWidth"))
    M.append(TempMeasure(measure.belowButtockToheel,
                         "below Buttock To heel", "belowButtockToheel"))
    M.append(TempMeasure(measure.frontWaistToHeel,
                         "front Waist To Heel", "frontWaistToHeel"))
    M.append(TempMeasure(measure.frontWaistToBelowKnee,
                         "front Waist To Below Knee", "frontWaistToBelowKnee"))
    M.append(TempMeasure(measure.NeckToWaist, "Neck To Waist", "NeckToWaist"))
    M.append(TempMeasure(measure.waistToCrotchLine,
                         "waist To Crotch Line", "waistToCrotchLine"))
    M.append(TempMeasure(measure.underBustToWaist,
                         "under Bust To Waist", "underBustToWaist"))
    M.append(TempMeasure(measure.rise, "rise", "rise"))
    M.append(TempMeasure(measure.NapeToWaist, "Nape To Waist", "NapeToWaist"))
    M.append(TempMeasure(measure.neckToShoulder,
                         "neck To Shoulder", "neckToShoulder"))

    M.append(TempMeasure(measure.underarmToWaist,
                         "underarm To Waist", "underarmToWaist"))

    fn = measure.first_name
    ln = measure.last_name

    if request.method == 'POST':
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]

        measure.first_name = fn
        measure.last_name = ln

        braSize = request.POST["braSize"]
        if braSize != measure.braSize:
            measure.braSize = braSize

        height = request.POST["height"]
        if height != measure.height:
            measure.height = height

        head = request.POST["head"]
        if head != measure.head:
            measure.head = head

        neck = request.POST["neck"]
        if neck != measure.neck:
            measure.neck = neck

        upperBust = request.POST["upperBust"]
        if upperBust != measure.upperBust:
            measure.upperBust = upperBust

        bust = request.POST["bust"]
        if bust != measure.bust:
            measure.bust = bust

        nippleToNipple = request.POST["nippleToNipple"]
        if nippleToNipple != measure.nippleToNipple:
            measure.nippleToNipple = nippleToNipple

        nippleToShoulder = request.POST["nippleToShoulder"]
        if nippleToShoulder != measure.nippleToShoulder:
            measure.nippleToShoulder = nippleToShoulder

        underBust = request.POST["underBust"]
        if underBust != measure.underBust:
            measure.underBust = underBust

        waist = request.POST["waist"]
        if waist != measure.waist:
            measure.waist = waist

        highHip = request.POST["highHip"]
        if highHip != measure.highHip:
            measure.highHip = highHip

        hip = request.POST["hip"]
        if hip != measure.hip:
            measure.hip = hip

        shoulderWidth = request.POST["shoulderWidth"]
        if shoulderWidth != measure.shoulderWidth:
            measure.shoulderWidth = shoulderWidth

        bicep = request.POST["bicep"]
        if bicep != measure.bicep:
            measure.bicep = bicep

        wrist = request.POST["wrist"]
        if wrist != measure.wrist:
            measure.wrist = wrist

        insideArm = request.POST["insideArm"]
        if insideArm != measure.insideArm:
            measure.insideArm = insideArm

        aroundKnuckle = request.POST["aroundKnuckle"]
        if aroundKnuckle != measure.aroundKnuckle:
            measure.aroundKnuckle = aroundKnuckle

        topOfThigh = request.POST["topOfThigh"]
        if topOfThigh != measure.topOfThigh:
            measure.topOfThigh = topOfThigh

        insideLegToHeel = request.POST["insideLegToHeel"]
        if insideLegToHeel != measure.insideLegToHeel:
            measure.insideLegToHeel = insideLegToHeel

        aroundKnee = request.POST["aroundKnee"]
        if aroundKnee != measure.aroundKnee:
            measure.aroundKnee = aroundKnee

        aroundCalf = request.POST["aroundCalf"]
        if aroundCalf != measure.aroundCalf:
            measure.aroundCalf = aroundCalf

        aroundAnkle = request.POST["aroundAnkle"]
        if aroundAnkle != measure.aroundAnkle:
            measure.aroundAnkle = aroundAnkle

        footWidth = request.POST["footWidth"]
        if footWidth != measure.footWidth:
            measure.footWidth = footWidth

        belowButtockToheel = request.POST["belowButtockToheel"]
        if belowButtockToheel != measure.belowButtockToheel:
            measure.belowButtockToheel = belowButtockToheel

        frontWaistToHeel = request.POST["frontWaistToHeel"]
        if frontWaistToHeel != measure.frontWaistToHeel:
            measure.frontWaistToHeel = frontWaistToHeel

        frontWaistToBelowKnee = request.POST["frontWaistToBelowKnee"]
        if frontWaistToBelowKnee != measure.frontWaistToBelowKnee:
            measure.frontWaistToBelowKnee = frontWaistToBelowKnee

        NeckToWaist = request.POST["NeckToWaist"]
        if NeckToWaist != measure.NeckToWaist:
            measure.NeckToWaist = NeckToWaist

        waistToCrotchLine = request.POST["waistToCrotchLine"]
        if waistToCrotchLine != measure.waistToCrotchLine:
            measure.waistToCrotchLine = waistToCrotchLine

        underBustToWaist = request.POST["underBustToWaist"]
        if underBustToWaist != measure.underBustToWaist:
            measure.underBustToWaist = underBustToWaist

        rise = request.POST["rise"]
        if rise != measure.rise:
            measure.rise = rise

        NapeToWaist = request.POST["NapeToWaist"]
        if NapeToWaist != measure.NapeToWaist:
            measure.NapeToWaist = NapeToWaist

        neckToShoulder = request.POST["neckToShoulder"]
        if neckToShoulder != measure.neckToShoulder:
            measure.neckToShoulder = neckToShoulder

        underarmToWaist = request.POST["underarmToWaist"]
        if underarmToWaist != measure.underarmToWaist:
            measure.underarmToWaist = underarmToWaist

        measure.save()

        return redirect('/dashboard')

    else:
        return render(request, 'addCustomer.html', {'Measure': M, 'fn': fn, 'ln': ln})


def customerMeasurements(request):
    measure = Measurements.objects.get(pk=request.POST["id"])
    fn = measure.first_name
    ln = measure.last_name
    ID = request.POST["id"]
    M = []
    M.append(TempMeasure(measure.braSize, "bra size", "braSize"))
    M.append(TempMeasure(measure.height, "height", "height"))
    M.append(TempMeasure(measure.head, "head", "head"))
    M.append(TempMeasure(measure.neck, "neck", "neck"))
    M.append(TempMeasure(measure.upperBust, "upper Bust", "upperBust"))
    M.append(TempMeasure(measure.bust, "bust", "bust"))
    M.append(TempMeasure(measure.nippleToNipple,
                         "nipple To Nipple", "nippleToNipple"))
    M.append(TempMeasure(measure.nippleToShoulder,
                         "nipple To Shoulder", "nippleToShoulder"))
    M.append(TempMeasure(measure.underBust, "under Bust", "underBust"))
    M.append(TempMeasure(measure.waist, "waist", "waist"))
    M.append(TempMeasure(measure.highHip, "highHip", "highHip"))
    M.append(TempMeasure(measure.hip, "hip", "hip"))
    M.append(TempMeasure(measure.shoulderWidth,
                         "shoulder Width", "shoulderWidth"))
    M.append(TempMeasure(measure.bicep, "bicep", "bicep"))
    M.append(TempMeasure(measure.wrist, "wrist", "wrist"))
    M.append(TempMeasure(measure.insideArm, "insideArm", "insideArm"))
    M.append(TempMeasure(measure.aroundKnuckle,
                         "around Knuckle", "aroundKnuckle"))
    M.append(TempMeasure(measure.topOfThigh, "top Of Thigh", "topOfThigh"))
    M.append(TempMeasure(measure.insideLegToHeel,
                         "inside Leg To Heel", "insideLegToHeel"))
    M.append(TempMeasure(measure.aroundKnee, "around Knee", "aroundKnee"))
    M.append(TempMeasure(measure.aroundCalf, "around Calf", "aroundCalf"))
    M.append(TempMeasure(measure.aroundAnkle, "around Ankle", "aroundAnkle"))
    M.append(TempMeasure(measure.footWidth, "foot Width", "footWidth"))
    M.append(TempMeasure(measure.belowButtockToheel,
                         "below Buttock To heel", "belowButtockToheel"))
    M.append(TempMeasure(measure.frontWaistToHeel,
                         "front Waist To Heel", "frontWaistToHeel"))
    M.append(TempMeasure(measure.frontWaistToBelowKnee,
                         "front Waist To Below Knee", "frontWaistToBelowKnee"))
    M.append(TempMeasure(measure.NeckToWaist, "Neck To Waist", "NeckToWaist"))
    M.append(TempMeasure(measure.waistToCrotchLine,
                         "waist To Crotch Line", "waistToCrotchLine"))
    M.append(TempMeasure(measure.underBustToWaist,
                         "under Bust To Waist", "underBustToWaist"))
    M.append(TempMeasure(measure.rise, "rise", "rise"))
    M.append(TempMeasure(measure.NapeToWaist, "Nape To Waist", "NapeToWaist"))
    M.append(TempMeasure(measure.neckToShoulder,
                         "neck To Shoulder", "neckToShoulder"))

    M.append(TempMeasure(measure.underarmToWaist,
                         "underarm To Waist", "underarmToWaist"))

    return render(request, 'customerMeasurements.html', {'Measure': M, 'fn': fn, 'ln': ln, 'id':ID})


def edit(request):
    ID = request.POST["id"]
    measure = Measurements.objects.get(pk=ID)
    fn = measure.first_name
    ln = measure.last_name
    M = []
    M.append(TempMeasure(measure.braSize, "bra size", "braSize"))
    M.append(TempMeasure(measure.height, "height", "height"))
    M.append(TempMeasure(measure.head, "head", "head"))
    M.append(TempMeasure(measure.neck, "neck", "neck"))
    M.append(TempMeasure(measure.upperBust, "upper Bust", "upperBust"))
    M.append(TempMeasure(measure.bust, "bust", "bust"))
    M.append(TempMeasure(measure.nippleToNipple,
                         "nipple To Nipple", "nippleToNipple"))
    M.append(TempMeasure(measure.nippleToShoulder,
                         "nipple To Shoulder", "nippleToShoulder"))
    M.append(TempMeasure(measure.underBust, "under Bust", "underBust"))
    M.append(TempMeasure(measure.waist, "waist", "waist"))
    M.append(TempMeasure(measure.highHip, "highHip", "highHip"))
    M.append(TempMeasure(measure.hip, "hip", "hip"))
    M.append(TempMeasure(measure.shoulderWidth,
                         "shoulder Width", "shoulderWidth"))
    M.append(TempMeasure(measure.bicep, "bicep", "bicep"))
    M.append(TempMeasure(measure.wrist, "wrist", "wrist"))
    M.append(TempMeasure(measure.insideArm, "insideArm", "insideArm"))
    M.append(TempMeasure(measure.aroundKnuckle,
                         "around Knuckle", "aroundKnuckle"))
    M.append(TempMeasure(measure.topOfThigh, "top Of Thigh", "topOfThigh"))
    M.append(TempMeasure(measure.insideLegToHeel,
                         "inside Leg To Heel", "insideLegToHeel"))
    M.append(TempMeasure(measure.aroundKnee, "around Knee", "aroundKnee"))
    M.append(TempMeasure(measure.aroundCalf, "around Calf", "aroundCalf"))
    M.append(TempMeasure(measure.aroundAnkle, "around Ankle", "aroundAnkle"))
    M.append(TempMeasure(measure.footWidth, "foot Width", "footWidth"))
    M.append(TempMeasure(measure.belowButtockToheel,
                         "below Buttock To heel", "belowButtockToheel"))
    M.append(TempMeasure(measure.frontWaistToHeel,
                         "front Waist To Heel", "frontWaistToHeel"))
    M.append(TempMeasure(measure.frontWaistToBelowKnee,
                         "front Waist To Below Knee", "frontWaistToBelowKnee"))
    M.append(TempMeasure(measure.NeckToWaist, "Neck To Waist", "NeckToWaist"))
    M.append(TempMeasure(measure.waistToCrotchLine,
                         "waist To Crotch Line", "waistToCrotchLine"))
    M.append(TempMeasure(measure.underBustToWaist,
                         "under Bust To Waist", "underBustToWaist"))
    M.append(TempMeasure(measure.rise, "rise", "rise"))
    M.append(TempMeasure(measure.NapeToWaist, "Nape To Waist", "NapeToWaist"))
    M.append(TempMeasure(measure.neckToShoulder,
                         "neck To Shoulder", "neckToShoulder"))

    M.append(TempMeasure(measure.underarmToWaist,
                         "underarm To Waist", "underarmToWaist"))
    
    
    if request.POST["EditNow"] == '1':
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]
        
        if ln != measure.last_name:
            Measurements.objects.filter(id=ID).update(last_name=ln)
        
        if fn != measure.first_name:
            Measurements.objects.filter(id=ID).update(first_name=fn)
        

        braSize = request.POST["braSize"]
        if braSize != measure.braSize:
            Measurements.objects.filter(
                id=ID).update(braSize=braSize)

        height = request.POST["height"]
        if height != measure.height:
            Measurements.objects.filter(
                id=ID).update(height=height)

        head = request.POST["head"]
        if head != measure.head:
            Measurements.objects.filter(
                id=ID).update(head=head)

        neck = request.POST["neck"]
        if neck != measure.neck:
            Measurements.objects.filter(
                id=ID).update(neck=neck)

        upperBust = request.POST["upperBust"]
        if upperBust != measure.upperBust:
            Measurements.objects.filter(
                id=ID).update(upperBust=upperBust)

        bust = request.POST["bust"]
        if bust != measure.bust:
            Measurements.objects.filter(
                id=ID).update(bust=bust)

        nippleToNipple = request.POST["nippleToNipple"]
        if nippleToNipple != measure.nippleToNipple:
            Measurements.objects.filter(
                id=ID).update(nippleToNipple=nippleToNipple)

        nippleToShoulder = request.POST["nippleToShoulder"]
        if nippleToShoulder != measure.nippleToShoulder:
            Measurements.objects.filter(
                id=ID).update(nippleToShoulder=nippleToShoulder)

        underBust = request.POST["underBust"]
        if underBust != measure.underBust:
            Measurements.objects.filter(
                id=ID).update(underBust=underBust)

        waist = request.POST["waist"]
        if waist != measure.waist:
            Measurements.objects.filter(
                id=ID).update(waist=waist)

        highHip = request.POST["highHip"]
        if highHip != measure.highHip:
            Measurements.objects.filter(
                id=ID).update(highHip=highHip)

        hip = request.POST["hip"]
        if hip != measure.hip:
            Measurements.objects.filter(
                id=ID).update(hip=hip)

        shoulderWidth = request.POST["shoulderWidth"]
        if shoulderWidth != measure.shoulderWidth:
            Measurements.objects.filter(
                id=ID).update(shoulderWidth=shoulderWidth)

        bicep = request.POST["bicep"]
        if bicep != measure.bicep:
            Measurements.objects.filter(
                id=ID).update(bicep=bicep)

        wrist = request.POST["wrist"]
        if wrist != measure.wrist:
            Measurements.objects.filter(
                id=ID).update(wrist=wrist)

        insideArm = request.POST["insideArm"]
        if insideArm != measure.insideArm:
            Measurements.objects.filter(
                id=ID).update(insideArm=insideArm)

        aroundKnuckle = request.POST["aroundKnuckle"]
        if aroundKnuckle != measure.aroundKnuckle:
            Measurements.objects.filter(
                id=ID).update(aroundKnuckle=aroundKnuckle)

        topOfThigh = request.POST["topOfThigh"]
        if topOfThigh != measure.topOfThigh:
            Measurements.objects.filter(
                id=ID).update(topOfThigh=topOfThigh)

        insideLegToHeel = request.POST["insideLegToHeel"]
        if insideLegToHeel != measure.insideLegToHeel:
            Measurements.objects.filter(
                id=ID).update(insideLegToHeel=insideLegToHeel)

        aroundKnee = request.POST["aroundKnee"]
        if aroundKnee != measure.aroundKnee:
            Measurements.objects.filter(
                id=ID).update(aroundKnee=aroundKnee)

        aroundCalf = request.POST["aroundCalf"]
        if aroundCalf != measure.aroundCalf:
            Measurements.objects.filter(
                id=ID).update(aroundCalf=aroundCalf)

        aroundAnkle = request.POST["aroundAnkle"]
        if aroundAnkle != measure.aroundAnkle:
            Measurements.objects.filter(
                id=ID).update(aroundAnkle=aroundAnkle)

        footWidth = request.POST["footWidth"]
        if footWidth != measure.footWidth:
            Measurements.objects.filter(
                id=ID).update(footWidth=footWidth)

        belowButtockToheel = request.POST["belowButtockToheel"]
        if belowButtockToheel != measure.belowButtockToheel:
            Measurements.objects.filter(
                id=ID).update(belowButtockToheel=belowButtockToheel)

        frontWaistToHeel = request.POST["frontWaistToHeel"]
        if frontWaistToHeel != measure.frontWaistToHeel:
            Measurements.objects.filter(
                id=ID).update(frontWaistToHeel=frontWaistToHeel)

        frontWaistToBelowKnee = request.POST["frontWaistToBelowKnee"]
        if frontWaistToBelowKnee != measure.frontWaistToBelowKnee:
            Measurements.objects.filter(
                id=ID).update(frontWaistToBelowKnee=frontWaistToBelowKnee)

        NeckToWaist = request.POST["NeckToWaist"]
        if NeckToWaist != measure.NeckToWaist:
            Measurements.objects.filter(
                id=ID).update(NeckToWaist=NeckToWaist)

        waistToCrotchLine = request.POST["waistToCrotchLine"]
        if waistToCrotchLine != measure.waistToCrotchLine:
            Measurements.objects.filter(
                id=ID).update(waistToCrotchLine=waistToCrotchLine)

        underBustToWaist = request.POST["underBustToWaist"]
        if underBustToWaist != measure.underBustToWaist:
            Measurements.objects.filter(
                id=ID).update(underBustToWaist=underBustToWaist)

        rise = request.POST["rise"]
        if rise != measure.rise:
            Measurements.objects.filter(
                id=ID).update(rise=rise)

        NapeToWaist = request.POST["NapeToWaist"]
        if NapeToWaist != measure.NapeToWaist:
            Measurements.objects.filter(
                id=ID).update(NapeToWaist=NapeToWaist)

        neckToShoulder = request.POST["neckToShoulder"]
        if neckToShoulder != measure.neckToShoulder:
            Measurements.objects.filter(
                id=ID).update(neckToShoulder=neckToShoulder)

        underarmToWaist = request.POST["underarmToWaist"]
        if underarmToWaist != measure.underarmToWaist:
            Measurements.objects.filter(
                id=ID).update(underarmToWaist=underarmToWaist)
        
        return redirect('/dashboard')

    else:
        return render(request, 'edit.html', {'Measure': M, 'fn': fn, 'ln': ln, 'id':ID})


def index(request):
    dresses = DressesImages.objects.all()
    handWorks = HandWorkImages.objects.all()
    chaniyaCholis = ChaniyaCholiImages.objects.all()
    blouses = BlouseImages.objects.all()

    return render(request, 'index.html', {'dresses': dresses, 'handWorks': handWorks, 'chaniyaCholis': chaniyaCholis, 'blouses': blouses})


def dashboard(request):

    if request.user.is_superuser:
        users = Measurements.objects.all()
        return render(request, 'dashboard.html', {'users': users})

    else:
        if not request.user.is_authenticated:
            return redirect('/')
        measure = Measurements.objects.get(pk=request.user.id)
        M = []
        M.append(TempMeasure(measure.braSize, "bra size", "braSize"))
        M.append(TempMeasure(measure.height, "height", "height"))
        M.append(TempMeasure(measure.head, "head", "head"))
        M.append(TempMeasure(measure.neck, "neck", "neck"))
        M.append(TempMeasure(measure.upperBust, "upper Bust", "upperBust"))
        M.append(TempMeasure(measure.bust, "bust", "bust"))
        M.append(TempMeasure(measure.nippleToNipple,
                             "nipple To Nipple", "nippleToNipple"))
        M.append(TempMeasure(measure.nippleToShoulder,
                             "nipple To Shoulder", "nippleToShoulder"))
        M.append(TempMeasure(measure.underBust, "under Bust", "underBust"))
        M.append(TempMeasure(measure.waist, "waist", "waist"))
        M.append(TempMeasure(measure.highHip, "highHip", "highHip"))
        M.append(TempMeasure(measure.hip, "hip", "hip"))
        M.append(TempMeasure(measure.shoulderWidth,
                             "shoulder Width", "shoulderWidth"))
        M.append(TempMeasure(measure.bicep, "bicep", "bicep"))
        M.append(TempMeasure(measure.wrist, "wrist", "wrist"))
        M.append(TempMeasure(measure.insideArm, "insideArm", "insideArm"))
        M.append(TempMeasure(measure.aroundKnuckle,
                             "around Knuckle", "aroundKnuckle"))
        M.append(TempMeasure(measure.topOfThigh, "top Of Thigh", "topOfThigh"))
        M.append(TempMeasure(measure.insideLegToHeel,
                             "inside Leg To Heel", "insideLegToHeel"))
        M.append(TempMeasure(measure.aroundKnee, "around Knee", "aroundKnee"))
        M.append(TempMeasure(measure.aroundCalf, "around Calf", "aroundCalf"))
        M.append(TempMeasure(measure.aroundAnkle,
                             "around Ankle", "aroundAnkle"))
        M.append(TempMeasure(measure.footWidth, "foot Width", "footWidth"))
        M.append(TempMeasure(measure.belowButtockToheel,
                             "below Buttock To heel", "belowButtockToheel"))
        M.append(TempMeasure(measure.frontWaistToHeel,
                             "front Waist To Heel", "frontWaistToHeel"))
        M.append(TempMeasure(measure.frontWaistToBelowKnee,
                             "front Waist To Below Knee", "frontWaistToBelowKnee"))
        M.append(TempMeasure(measure.NeckToWaist,
                             "Neck To Waist", "NeckToWaist"))
        M.append(TempMeasure(measure.waistToCrotchLine,
                             "waist To Crotch Line", "waistToCrotchLine"))
        M.append(TempMeasure(measure.underBustToWaist,
                             "under Bust To Waist", "underBustToWaist"))
        M.append(TempMeasure(measure.rise, "rise", "rise"))
        M.append(TempMeasure(measure.NapeToWaist,
                             "Nape To Waist", "NapeToWaist"))
        M.append(TempMeasure(measure.neckToShoulder,
                             "neck To Shoulder", "neckToShoulder"))

        M.append(TempMeasure(measure.underarmToWaist,
                             "underarm To Waist", "underarmToWaist"))

        return render(request, 'dashboard.html', {'m': M})


def resetPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'resetPassword.html', {'form': form})


def Signin(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        unn = request.POST['username']
        pa = request.POST['password']
        user = auth.authenticate(username=unn, password=pa)
        if user is None:
            messages.info(request, 'Invalide Username or Password')
            return render(request, 'signin.html')

        else:
            auth.login(request, user)
            return redirect('/dashboard')

    else:
        return render(request, 'signin.html')


def Signout(request):
    auth.logout(request)
    return redirect('/')
