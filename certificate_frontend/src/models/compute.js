export default class compute{
    static convertFromScale(input) {
        switch (input) {
            case 2:
                return "High"
            case 1:
                return "Medium"
            case 0:
                return "Low"
        }

    }

    static convertFromBool(input) {
        switch (input) {
            case 1:
                return true
            case 0:
                return false
        }

    }
}