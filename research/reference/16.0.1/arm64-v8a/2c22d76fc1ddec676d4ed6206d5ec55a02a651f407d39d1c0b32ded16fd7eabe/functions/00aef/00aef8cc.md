# 00aef8cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aef8cc",
  "name": "FUN_00aef8cc",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36d14bd72d07d817a6ff1a30ec311b29457ced7c852c66feb94b5a40844b3d3c",
  "source_text_sha256": "36d14bd72d07d817a6ff1a30ec311b29457ced7c852c66feb94b5a40844b3d3c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b6f18](../008b6/008b6f18.md)
- [008b79c8](../008b7/008b79c8.md)
- [008b9178](../008b9/008b9178.md)

## 疑似コード / UTF-8 2084 bytes

~~~c

void FUN_00aef8cc(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  int iVar1;
  uint uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined4 uVar5;
  long lVar6;
  
  iVar1 = *param_3;
  uVar2 = *param_4;
                    /* try { // try from 00aef8e0 to 00bef95f has its CatchHandler @ 00aef8e0
                       catch() { ... } // from try @ 00aef8e0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aef968 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aef9e0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefa58 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefad0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefb50 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefbd0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefc4c with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefd9c with catch @ 00aef8e0 */
  lVar6 = *(long *)(param_1 + 8);
  if (iVar1 == 5) {
    if (uVar2 < 2) {
      uVar3 = FUN_0047acf4();
      FUN_0047cdd4(uVar3,0xb,0);
      *(int *)(lVar6 + 0x1188) = *(int *)(lVar6 + 0x1188) + 1;
      if (uVar2 == 0) {
        uVar5 = 1;
      }
      else {
        uVar5 = 2;
      }
      *(undefined4 *)(lVar6 + 0x118c) = uVar5;
    }
  }
  else if (iVar1 == 3) {
    if (uVar2 < 2) {
      uVar3 = FUN_0047acf4();
                    /* try { // try from 00aef960 to 00bef967 has its CatchHandler @ 00aefdb8 */
                    /* try { // try from 00aef968 to 00bef9d7 has its CatchHandler @ 00aef8e0 */
      FUN_0047cdd4(uVar3,0xf,0);
      return;
    }
  }
  else if (iVar1 == 2) {
    uVar3 = *param_2;
    if (1 < uVar2) {
      if (uVar2 != 0xfffffffe) {
        return;
      }
      uVar4 = FUN_0047acf4(uVar3);
      FUN_0047cdd4(uVar4,0xb,0);
    }
    FUN_008b9178(uVar3);
    uVar3 = FUN_008b79c8(lVar6 + 0x2f38,0x326);
    FUN_008b6f18(uVar3,0);
    return;
  }
  return;
}

~~~
