import laptops
import phones
import classifier

def rough_prediction(category, ram, storage, yor, age, scrd, chrgav, keywork, batth):
    if category == "laptop":
        #print("laptop")
        predict_points = laptops.predict(ram, storage, yor, age, scrd, chrgav, keywork, batth)
        return predict_points
    elif category == 'cell phone':
        predict_points = phones.predict(ram, storage, yor, age, scrd, chrgav, keywork, batth)
        return predict_points
    else:
        return 50

#[hasDamage, hasScratches, hasDents, ColorWearedOff, software (1 for ios and 0 for android), loyalty], 
#rest all 0 for no and 1 for yes
def final_points(image, ram, storage, yor, age, scrd, chrgav, keywork, batth, a, b, c, d, e, f):
    category = classifier.detect(image)
    try:
        predicted_price = rough_prediction(category, ram, storage, yor, age, scrd, chrgav, keywork, batth)
        print("Predicted Price:", predicted_price)  # Print the predicted price
    except Exception as e:
        print("Error:", e)
        return 0  
    final_price = predicted_price
    if a:
        alpha = 0.6
        final_price *= alpha
    if b:
        beta = 0.9
        final_price *= beta
    if c:
        gamma = 0.6
        final_price *= gamma
    if d:
        delta = 0.9
        final_price *= delta
    if e:
        omega = 1.5
        final_price *= omega
    if f:
        eta = 1.075
        final_price *= eta
    if final_price > 1000:
        final_price = 1000

    if final_price < 100:
        final_price = 100
    final_points = int(final_price)
    print("Final Points:", final_points)  # Print the final points
    #return final_points

# Example usage
final_points('D:/ewaste_price_detection/Ewaste_price_prediction/image.png', 4, 64, 2014, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0)
