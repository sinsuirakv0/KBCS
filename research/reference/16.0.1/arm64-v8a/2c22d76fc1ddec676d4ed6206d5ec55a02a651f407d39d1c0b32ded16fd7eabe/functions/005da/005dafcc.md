# 005dafcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "005dafcc",
  "name": "FUN_005dafcc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5441e3eb3dcc468d150304dd26dd971b28cc11bb55ffc088435b956319a241cb",
  "source_text_sha256": "5441e3eb3dcc468d150304dd26dd971b28cc11bb55ffc088435b956319a241cb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b9178](../008b9/008b9178.md)

## 疑似コード / UTF-8 470 bytes

~~~c

void FUN_005dafcc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
                    /* try { // try from 005dafd8 to 006dafe3 has its CatchHandler @ 005db060 */
    uVar2 = *param_2;
    uVar1 = FUN_0047acf4();
    FUN_0047cdd4(uVar1,0xb,0);
                    /* try { // try from 005db004 to 006db00f has its CatchHandler @ 005db05c */
    FUN_008b9178(uVar2);
    return;
  }
  return;
}

~~~
