// get brower
export function get_current_browser () {
  let ua = navigator.userAgent.toLocaleLowerCase()
  let browserType = null
  if (ua.match(/msie/) != null || ua.match(/trident/) != null) {
    browserType = 'IE'
  } else if (ua.match(/firefox/) != null) {
    browserType = 'firefox'
  } else if (ua.match(/ucbrowser/) != null) {
    browserType = 'UC'
  } else if (ua.match(/opera/) != null || ua.match(/opr/) != null) {
    browserType = 'opera'
  } else if (ua.match(/bidubrowser/) != null) {
    browserType = 'baidu'
  } else if (ua.match(/metasr/) != null) {
    browserType = 'sougou'
  } else if (ua.match(/tencenttraveler/) != null || ua.match(/qqbrowse/) != null) {
    browserType = 'QQ'
  } else if (ua.match(/maxthon/) != null) {
    browserType = 'maxthon'
  } else if (ua.match(/chrome/) != null) {
    var is360 = _mime('type', 'application/vnd.chromium.remoting-viewer')
    if (is360) {
      browserType = '360'
    } else {
      browserType = 'chrome'
    }
  } else if (ua.match(/safari/) != null) {
    browserType = 'Safari'
  } else {
    browserType = 'others'
  }
  return browserType
}

function _mime (option, value) {
  var mimeTypes = navigator.mimeTypes
  for (var mt in mimeTypes) {
    if (mimeTypes[mt][option] === value) {
      return true
    }
  }
  return false
}

// get os
export function get_os () {
  let sUserAgent = navigator.userAgent.toLocaleLowerCase()
  let isWin = (navigator.platform.toLocaleLowerCase() === 'win32') || (navigator.platform.toLocaleLowerCase() === 'windows')|| (navigator.platform.toLocaleLowerCase() === 'win64')
  let isMac = (navigator.platform.toLocaleLowerCase() === 'mac68k') || (navigator.platform.toLocaleLowerCase() === 'macppc') || (navigator.platform.toLocaleLowerCase() === 'macintosh') || (navigator.platform.toLocaleLowerCase() === 'macintel')
  if (isMac) return 'Mac'
  var isUnix = (navigator.platform.toLocaleLowerCase() === 'x11') && !isWin && !isMac
  if (isUnix) return 'Unix'
  var isLinux = (String(navigator.platform.toLocaleLowerCase()).indexOf('linux') > -1)
  if (isLinux) return 'Linux'
  if (isWin) {
    var isWin2K = sUserAgent.indexOf('windows nt 5.0') > -1 || sUserAgent.indexOf('windows 2000') > -1
    if (isWin2K) return 'Win2000'
    var isWinXP = sUserAgent.indexOf('windows nt 5.1') > -1 || sUserAgent.indexOf('windows xp') > -1
    if (isWinXP) return 'WinXP'
    var isWin2003 = sUserAgent.indexOf('windows nt 5.2') > -1 || sUserAgent.indexOf('windows 2003') > -1
    if (isWin2003) return 'Win2003'
    var isWinVista = sUserAgent.indexOf('windows nt 6.0') > -1 || sUserAgent.indexOf('windows vista') > -1
    if (isWinVista) return 'WinVista'
    var isWin7 = sUserAgent.indexOf('windows nt 6.1') > -1 || sUserAgent.indexOf('windows 7') > -1
    if (isWin7) return 'Win7'

    var isWin8 = sUserAgent.indexOf('windows nt 6.2') > -1 || sUserAgent.indexOf('windows 8') > -1
    if (isWin8) return 'Win8'

    var isWin81 = sUserAgent.indexOf('windows nt 6.3') > -1 || sUserAgent.indexOf('windows 8') > -1
    if (isWin81) return 'Win81'

    let isWin10 = sUserAgent.indexOf('windows nt 10.0') > -1 || sUserAgent.indexOf('windows 10') > -1
    if (isWin10) return 'Win10'



  }
  if (sUserAgent.indexOf('android') > -1) return 'Android'
  if (sUserAgent.indexOf('iphone') > -1) return 'iPhone'
  if (sUserAgent.indexOf('symbianos') > -1) return 'SymbianOS'
  if (sUserAgent.indexOf('windows phone') > -1) return 'Windows Phone'
  if (sUserAgent.indexOf('ipad') > -1) return 'iPad'
  if (sUserAgent.indexOf('ipod') > -1) return 'iPod'
  console.log(sUserAgent)
  return 'others'
}

// getAddress
document.write("<script src=\"http://pv.sohu.com/cityjson?ie=utf-8\"></script>");

export async function get_address () {
  let sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));
  let retry_count = 100
  while (typeof returnCitySN == "undefined") {
    retry_count--
     console.log("retry:",retry_count)
    if (retry_count == 0){
      return ""
    }
    await sleep(200)
  }
  return returnCitySN["cip"]
}

export async function get_city () {
  let sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));
  let retry_count = 100
  while (typeof returnCitySN == "undefined") {
    retry_count--
    console.log("retry:",retry_count)
    if (retry_count == 0){
      return ""
    }
    await sleep(200)

  }
  return returnCitySN["cname"]
}




