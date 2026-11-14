# 00af4cec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af4cec",
  "name": "FUN_00af4cec",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a7f5ca513c426055eda8231a69f6af0d39e01ce368bfa3bdfb3b2782b9e745c",
  "source_text_sha256": "4a7f5ca513c426055eda8231a69f6af0d39e01ce368bfa3bdfb3b2782b9e745c"
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)
- [006bc0a0](../006bc/006bc0a0.md)
- [00700f00](../00700/00700f00.md)
- [00715908](../00715/00715908.md)
- [00716e98](../00716/00716e98.md)
- [00716f88](../00716/00716f88.md)
- [00717198](../00717/00717198.md)
- [00a50418](../00a50/00a50418.md)
- [00a53028](../00a53/00a53028.md)

## 呼び出し先

- [0046db10](../0046d/0046db10.md)
- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 1271 bytes

~~~c

void FUN_00af4cec(int param_1,int param_2,int param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  
  if (param_3 == 0) {
    lVar2 = FUN_008524fc();
    if (*(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848f0) == 0) {
      param_3 = 1;
    }
    else {
      lVar2 = FUN_008524fc();
      uVar4 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
      if ((uVar4 & 1) == 0) {
        lVar2 = FUN_008524fc();
        param_3 = 0xe;
        if (*(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bfc) < 1) {
          param_3 = 0;
        }
      }
      else {
        param_3 = 0;
      }
    }
  }
  else if (param_3 == 4) {
    lVar2 = FUN_008524fc();
    if (*(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bb0) != 0) {
      iVar1 = FUN_0046db10(100);
      lVar2 = FUN_008524fc();
      if (iVar1 < *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bb0)) {
        uVar3 = FUN_0047b054();
        FUN_0047d134(uVar3,0x8f,0);
        param_3 = 0x15;
        goto LAB_00af4e24;
      }
    }
    param_3 = 4;
  }
LAB_00af4e24:
  lVar2 = FUN_008524fc();
  *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) = param_3;
  return;
}

~~~
