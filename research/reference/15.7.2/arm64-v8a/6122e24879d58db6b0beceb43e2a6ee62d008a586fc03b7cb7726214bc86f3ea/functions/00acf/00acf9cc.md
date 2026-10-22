# 00acf9cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acf9cc.md)

## 関数情報

~~~json
{
  "address": "00acf9cc",
  "name": "FUN_00acf9cc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a277d5cc502b76a5ffbb00d297c95fbd8f9c630d9280d8ef1fae870fe9a3860f",
  "source_text_sha256": "a277d5cc502b76a5ffbb00d297c95fbd8f9c630d9280d8ef1fae870fe9a3860f"
}
~~~
## 呼び出し元

- [0058b674](../0058b/0058b674.md)
- [005d8f58](../005d8/005d8f58.md)
- [00617dec](../00617/00617dec.md)
- [00624a0c](../00624/00624a0c.md)
- [0062da7c](../0062d/0062da7c.md)
- [0063eb28](../0063e/0063eb28.md)
- [00680234](../00680/00680234.md)
- [00680a7c](../00680/00680a7c.md)
- [006a7120](../006a7/006a7120.md)
- [006aef04](../006ae/006aef04.md)
- [006d6d04](../006d6/006d6d04.md)
- [0072f3c8](../0072f/0072f3c8.md)
- [00730204](../00730/00730204.md)
- [00733374](../00733/00733374.md)
- [0088f740](../0088f/0088f740.md)
- [008a76c0](../008a7/008a76c0.md)
- [008b9174](../008b9/008b9174.md)
- [008be650](../008be/008be650.md)
- [0092bc08](../0092b/0092bc08.md)
- [0092d380](../0092d/0092d380.md)
- [0094f64c](../0094f/0094f64c.md)
- [0094f7d0](../0094f/0094f7d0.md)
- [00957320](../00957/00957320.md)
- [00957f9c](../00957/00957f9c.md)
- [009613bc](../00961/009613bc.md)
- [00963004](../00963/00963004.md)
- [00a26cbc](../00a26/00a26cbc.md)
- [00a271c8](../00a27/00a271c8.md)
- [00a28640](../00a28/00a28640.md)
- [00a28744](../00a28/00a28744.md)
- [00a72648](../00a72/00a72648.md)
- [00a7888c](../00a78/00a7888c.md)
- [00a82394](../00a82/00a82394.md)

## 呼び出し先

- [00adbf88](../00adb/00adbf88.md)

## 疑似コード 1/1 / UTF-8 377 bytes

~~~c

int FUN_00acf9cc(undefined8 param_1)

{
  uint uVar1;
  uint uVar2;
  undefined8 uVar3;
  
  uVar3 = FUN_00adbf88();
  uVar1 = 50000;
  if ((uint)uVar3 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar3 >> 0x10) & 0xffff;
  }
  uVar2 = FUN_00adbf88(param_1);
  uVar2 = uVar2 & 0xffff;
  if (49999 < uVar2) {
    uVar2 = 50000;
  }
  return uVar2 + uVar1;
}

~~~
