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
}