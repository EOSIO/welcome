---
title: "Datastream"
excerpt: "Defines data stream for reading and writing data in the form of bytes."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public template<>`  <br/>`inline datastream< Stream > & `[`operator<<`](#operator<<)`(datastream< Stream > & ds,const `[`public_key`](#public_key)` pubkey)`            | Serialize a [public_key](#public_key).
`public template<>`  <br/>`inline datastream< Stream > & `[`operator>>`](#operator>>)`(datastream< Stream > & ds,`[`public_key`](#public_key)` & pubkey)`            | Deserialize a [public_key](#public_key).
`public template<>`  <br/>`inline datastream< Stream > & `[`operator<<`](#operator<<)`(datastream< Stream > & ds,const key256 & d)`            | Serialize a key256.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator>>`](#operator>>)`(datastream< Stream > & ds,key256 & d)`            | Deserialize a key256.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator<<`](#operator<<)`(datastream< Stream > & ds,const bool & d)`            | Serialize a bool into a stream.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator>>`](#operator>>)`(datastream< Stream > & ds,bool & d)`            | Deserialize a bool.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator<<`](#operator<<)`(datastream< Stream > & ds,const checksum256 & d)`            | Serialize a checksum256.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator>>`](#operator>>)`(datastream< Stream > & ds,checksum256 & d)`            | Deserialize a checksum256.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const std::string & v)`            | Serialize a string.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,std::string & v)`            | Deserialize a string.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const std::array< T, `[`N`](#N)` > & v)`            | Serialize a fixed size array.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,std::array< T, `[`N`](#N)` > & v)`            | Deserialize a fixed size array.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,T)`            | Deserialize a a pointer.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const T(&) v)`            | Serialize a fixed size array of non-primitive and non-pointer type.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,T(&) v)`            | Deserialize a fixed size array of non-primitive and non-pointer type.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const vector< char > & v)`            | Serialize a vector of char.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const vector< T > & v)`            | Serialize a vector.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,vector< char > & v)`            | Deserialize a vector of char.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,vector< T > & v)`            | Deserialize a vector.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const std::set< T > & s)`            | 
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,std::set< T > & s)`            | 
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const std::map< K, V > & m)`            | Serialize a map.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,std::map< K, V > & m)`            | Deserialize a map.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const boost::container::flat_set< T > & s)`            | 
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,boost::container::flat_set< T > & s)`            | 
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const boost::container::flat_map< K, V > & m)`            | Serialize a flat map.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,boost::container::flat_map< K, V > & m)`            | Deserialize a flat map.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const std::tuple< Args... > & t)`            | Serialize a tuple.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,std::tuple< Args... > & t)`            | Deserialize a tuple.
`public template<>`  <br/>`DataStream & `[`operator<<`](#operator<<)`(DataStream & ds,const T & v)`            | Serialize a class.
`public template<>`  <br/>`DataStream & `[`operator>>`](#operator>>)`(DataStream & ds,T & v)`            | Deserialize a class.
`public template<>`  <br/>`T `[`unpack`](#unpack)`(const char * buffer,size_t len)`            | Unpack data inside a fixed size buffer as T.
`public template<>`  <br/>`T `[`unpack`](#unpack)`(const vector< char > & bytes)`            | Unpack data inside a variable size buffer as T.
`public template<>`  <br/>`size_t `[`pack_size`](#pack_size)`(const T & value)`            | Get the size of the packed data.
`public template<>`  <br/>`bytes `[`pack`](#pack)`(const T & value)`            | Get packed data.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator<<`](#operator<<)`(datastream< Stream > & ds,const checksum160 & cs)`            | Serialize a checksum160 type.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator>>`](#operator>>)`(datastream< Stream > & ds,checksum160 & cs)`            | Deserialize a checksum160 type.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator<<`](#operator<<)`(datastream< Stream > & ds,const checksum512 & cs)`            | Serialize a checksum512 type.
`public template<>`  <br/>`inline datastream< Stream > & `[`operator>>`](#operator>>)`(datastream< Stream > & ds,checksum512 & cs)`            | Deserialize a checksum512 type.
`class `[`eosio::datastream`](docs2/datastream.md#classeosio_1_1datastream) | A data stream for reading and writing data in the form of bytes.
`class `[`eosio::datastream< size_t >`](docs2/datastream.md#classeosio_1_1datastream_3_01size__t_01_4) | Specialization of datastream used to help determine the final size of a serialized value. Specialization of datastream used to help determine the final size of a serialized value.