# 007fcfdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "007fcfdc",
  "name": "FUN_007fcfdc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a109c46f4c557aa0e4e98bc4669cd1080940389109232a1c9dc24c919c1a8e42",
  "source_text_sha256": "a109c46f4c557aa0e4e98bc4669cd1080940389109232a1c9dc24c919c1a8e42"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [007efca8](../007ef/007efca8.md)
- [008b9178](../008b9/008b9178.md)

## 疑似コード / UTF-8 471 bytes

~~~c

void FUN_007fcfdc(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
    if (*param_4 < 2) {
      uVar2 = *param_2;
      uVar1 = FUN_0047acf4();
      FUN_0047cdd4(uVar1,0xb,0);
      FUN_008b9178(uVar2);
      return;
    }
  }
  else if ((*param_3 == 5) && (*param_4 == 0)) {
    FUN_007efca8(*(undefined8 *)(param_1 + 8),*(undefined4 *)(param_1 + 0x10),0);
    return;
  }
  return;
}

~~~
