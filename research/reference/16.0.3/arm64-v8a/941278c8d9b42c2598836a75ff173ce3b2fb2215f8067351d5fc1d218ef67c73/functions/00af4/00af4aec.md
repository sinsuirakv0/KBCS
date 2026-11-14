# 00af4aec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af4aec",
  "name": "FUN_00af4aec",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97665991fb00a6c9a82e41f61f099e67c6d4ca6011c4c233a84abee899826a29",
  "source_text_sha256": "97665991fb00a6c9a82e41f61f099e67c6d4ca6011c4c233a84abee899826a29"
}
~~~

## 呼び出し元

- [005f3e60](../005f3/005f3e60.md)
- [005fbd2c](../005fb/005fbd2c.md)
- [00713760](../00713/00713760.md)
- [00714664](../00714/00714664.md)
- [00714ff0](../00714/00714ff0.md)
- [007151c0](../00715/007151c0.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 関連文字列（未確認候補）

~~~text
"NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS6_ISB_EEFbRKNS_10shared_ptrIN2fs8FileDataEEEEEE"
"ZN11aDownloader8downloadERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEiiE3$_1"
"provider_id && id_token && raw_nonce"
~~~

## 疑似コード / UTF-8 2258 bytes

~~~c

void FUN_00af4aec(undefined8 *param_1,int param_2,int param_3)

{
  byte *pbVar1;
  byte bVar2;
  long lVar3;
  ulong uVar4;
  long lVar5;
  undefined1 uVar6;
  undefined4 uVar7;
  long lVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  
  lVar3 = FUN_008524fc();
  if ((*(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) == 0) ||
     (lVar3 = FUN_008524fc(),
     *(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) != 1)) {
    lVar3 = FUN_008524fc();
    if (*(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) != 0) {
      FUN_008524fc();
      lVar3 = FUN_008524fc();
      uVar4 = FUN_005e7810(lVar3 + (long)param_2 * 0x1f0 + 0x2768);
      lVar3 = FUN_008524fc();
      if ((uVar4 & 1) == 0) {
        lVar5 = FUN_008524fc();
        pbVar1 = (byte *)("provider_id && id_token && raw_nonce" +
                         lVar3 + (long)*(int *)(lVar5 + (long)param_2 * 0xc804 +
                                                (long)param_3 * 0x3ec + 0x848c8) * 0x18 + 7);
        bVar2 = *pbVar1;
      }
      else {
        lVar8 = (long)*(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) +
                -2;
        lVar3 = FUN_008524fc();
        lVar5 = FUN_008524fc();
        pbVar1 = (byte *)(
                         "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS6_ISB_EEFbRKNS_10shared_ptrIN2fs8FileDataEEEEEE"
                         + lVar3 + lVar8 * 0x1e0 +
                           (long)*(int *)(lVar5 + lVar8 * 4 + 0x49934) * 0x78 + 0xa2);
        bVar2 = *pbVar1;
      }
      if ((bVar2 & 1) == 0) {
        uVar10 = *(undefined8 *)(pbVar1 + 8);
        uVar9 = *(undefined8 *)pbVar1;
        param_1[2] = *(undefined8 *)(pbVar1 + 0x10);
        param_1[1] = uVar10;
        *param_1 = uVar9;
        return;
      }
      FUN_0043be80(param_1,*(undefined8 *)(pbVar1 + 0x10),*(undefined8 *)(pbVar1 + 8));
      return;
    }
    uVar6 = 8;
    *(undefined1 *)((long)param_1 + 5) = 0;
    uVar7 = 0x656e6f4e;
  }
  else {
    uVar6 = 6;
    uVar7 = 0x8e9fe5;
  }
  *(undefined1 *)param_1 = uVar6;
  *(undefined4 *)((long)param_1 + 1) = uVar7;
  return;
}

~~~
