# 00bca0bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bca0bc",
  "name": "_ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6dad339c43cab4b1b8b36f59e52d7668aace67c7c4ebf6a45eec1b52396ca425",
  "source_text_sha256": "6dad339c43cab4b1b8b36f59e52d7668aace67c7c4ebf6a45eec1b52396ca425"
}
~~~

## 呼び出し元

- [00c5a5c0](../00c5a/00c5a5c0.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ad30](../00c5a/00c5ad30.md)
- [00c5b1e0](../00c5b/00c5b1e0.md)
- [00c5d590](../00c5d/00c5d590.md)
- [00c5d5d0](../00c5d/00c5d5d0.md)
- [00c5d690](../00c5d/00c5d690.md)

## 関連文字列（未確認候補）

~~~text
"Creating Auth %p for App %p"
~~~

## 疑似コード / UTF-8 3373 bytes

~~~c

long _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE(ulong param_1,undefined4 *param_2)

{
  undefined *puVar1;
  long lVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  
  puVar1 = PTR__ZN8firebase4auth13g_auths_mutexE_00c9b5a0;
  uVar5 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9b5a0;
  _ZN8firebase5Mutex7AcquireEv(uVar5);
  uVar7 = *(undefined8 *)puVar1;
  _ZN8firebase5Mutex7AcquireEv(uVar7);
  puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9b5a8;
  puVar4 = *(undefined **)(PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8);
  if (puVar4 != (undefined *)0x0) {
    puVar3 = PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8;
    do {
      if (*(ulong *)(puVar4 + 0x20) >= param_1) {
        puVar3 = puVar4;
      }
      puVar4 = *(undefined **)(puVar4 + (ulong)(*(ulong *)(puVar4 + 0x20) < param_1) * 8);
    } while (puVar4 != (undefined *)0x0);
    if ((puVar3 != PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8) &&
       (*(ulong *)(puVar3 + 0x20) <= param_1)) {
      lVar6 = *(long *)(puVar3 + 0x28);
      goto LAB_00bca144;
    }
  }
  lVar6 = 0;
LAB_00bca144:
  _ZN8firebase5Mutex7ReleaseEv(uVar7);
  if (lVar6 == 0) {
    lVar2 = _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE(param_1);
    if (lVar2 == 0) {
      lVar6 = 0;
    }
    else {
      lVar6 = _Znwm(8);
      _ZN8firebase4auth4AuthC1EPNS_3AppEPv(lVar6,param_1,lVar2);
      _ZN8firebase8LogDebugEPKcz("Creating Auth %p for App %p",lVar6,param_1);
      puVar10 = (undefined8 *)(puVar1 + 8);
      if ((undefined8 *)*puVar10 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = puVar10;
      }
      else {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = (undefined8 *)(puVar1 + 8);
LAB_00bca1d8:
        do {
          puVar10 = puVar8;
          if ((ulong)puVar10[4] <= param_1) {
            if ((ulong)puVar10[4] < param_1) {
              puVar9 = puVar10 + 1;
              puVar8 = (undefined8 *)*puVar9;
              if ((undefined8 *)*puVar9 != (undefined8 *)0x0) goto LAB_00bca1d8;
            }
            puVar8 = (undefined8 *)*puVar9;
            goto joined_r0x00bca240;
          }
          puVar8 = (undefined8 *)*puVar10;
          puVar9 = puVar10;
        } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
        puVar8 = (undefined8 *)*puVar10;
      }
joined_r0x00bca240:
      if (puVar8 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)_Znwm(0x30);
        puVar8[4] = param_1;
        puVar8[5] = 0;
        *puVar8 = 0;
        puVar8[1] = 0;
        puVar8[2] = puVar10;
        *puVar9 = puVar8;
        puVar10 = puVar8;
        if (**(long **)puVar1 != 0) {
          *(long *)puVar1 = **(long **)puVar1;
          puVar10 = (undefined8 *)*puVar9;
        }
        _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
                  (*(undefined8 *)(puVar1 + 8),puVar10);
        *(long *)(puVar1 + 0x10) = *(long *)(puVar1 + 0x10) + 1;
      }
      puVar8[5] = lVar6;
      if (param_2 != (undefined4 *)0x0) {
        *param_2 = 0;
      }
    }
  }
  else {
    if (param_2 != (undefined4 *)0x0) {
      *param_2 = 0;
    }
    _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE(lVar6);
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar5);
  return lVar6;
}

~~~
