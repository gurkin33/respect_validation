validation_parser = {

  nested_validators: ['allOf', 'anyOf', 'noneOf', 'oneOf'],

  run: function(data) {
    output = {}

    for (const [key, value] of Object.entries(data)) {
      // console.log(`${key}: ${value}`);
      output[key] = null
      if (!value){
        console.log("Empty for", key)
        continue
      }
      output[key] = this.message_parser(value)
    }

    return output
  },

  message_parser: function(data){
    messages = []

    for (const [key, value] of Object.entries(data)) {
      // console.log(`${key}: ${value}`);
      if (!Array.isArray(value)){
        console.log('You are not array! ', value, ' for key', key)
      }
      for (let i = 0; i < value.length; i++){
        if (typeof value[i] === 'string' || value[i] instanceof String){
          messages[messages.length] = value[i]
        } else {
          messages = messages.concat(
            this.message_parser(value[i])
          );
        }
      }
    }

    return messages
  }
}
