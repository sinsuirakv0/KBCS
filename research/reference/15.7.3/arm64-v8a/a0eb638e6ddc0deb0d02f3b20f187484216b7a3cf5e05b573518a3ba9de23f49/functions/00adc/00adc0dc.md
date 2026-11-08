# 00adc0dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00adc0dc",
  "name": "FUN_00adc0dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "475c0d95432c2d38b7ccc53a5e26b4fb8edef1c47afac613649f58b1e13873a7",
  "source_text_sha256": "475c0d95432c2d38b7ccc53a5e26b4fb8edef1c47afac613649f58b1e13873a7"
}
~~~

## 呼び出し元

- [005b726c](../005b7/005b726c.md)
- [00670de0](../00670/00670de0.md)
- [006f4518](../006f4/006f4518.md)
- [008b0960](../008b0/008b0960.md)
- [008b11a4](../008b1/008b11a4.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

## 疑似コード / UTF-8 549 bytes

~~~c

void FUN_00adc0dc(byte *param_1,int param_2)

{
                    /* try { // try from 00adc0e4 to 00bdc203 has its CatchHandler @ 00adc0e4
                       catch() { ... } // from try @ 00adc0e4 with catch @ 00adc0e4
                       catch() { ... } // from try @ 00adc228 with catch @ 00adc0e4 */
  *(uint *)param_1 =
       (((uint)(param_1[5] ^ param_1[2]) << 0x10 | (uint)(param_1[4] ^ param_1[3]) << 0x18 |
        (uint)(param_1[6] ^ param_1[1]) << 8) - param_2) + (uint)(param_1[7] ^ *param_1);
  FUN_005c3468();
  return;
}

~~~
