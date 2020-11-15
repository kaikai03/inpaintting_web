const sizeUnits = ['B', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb'];

export default {
    numberToSize(num) {
        if (num < 1024) return num + 'B';
        let k = 1024, // or 1000
            i = Math.floor(Math.log(num) / Math.log(k));
        return (num / Math.pow(k, i)).toPrecision(5) + ' ' + sizeUnits[i];
    },
    addPercentSymbol(num) {
        return num + '%';
    }
}