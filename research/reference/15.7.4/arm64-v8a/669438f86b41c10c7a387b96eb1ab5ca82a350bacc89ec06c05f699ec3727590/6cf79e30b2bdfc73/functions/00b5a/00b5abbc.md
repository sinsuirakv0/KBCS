# 00b5abbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00b5abbc.md)

## 関数情報

~~~json
{
  "address": "00b5abbc",
  "name": "_ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47cb16451d2719fdeef769598553becb2e8892acd910cb31e4b743ddd773731c",
  "source_text_sha256": "47cb16451d2719fdeef769598553becb2e8892acd910cb31e4b743ddd773731c"
}
~~~
## 呼び出し元

- [00bddb70](../00bdd/00bddb70.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bde2b0](../00bde/00bde2b0.md)
- [00bde760](../00bde/00bde760.md)
- [00be0990](../00be0/00be0990.md)
- [00be09d0](../00be0/00be09d0.md)
- [00be0a90](../00be0/00be0a90.md)

## 関連文字列（未確認候補）

~~~text
"Creating Auth %p for App %p"
~~~
## 疑似コード 1/1 / UTF-8 3664 bytes

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
  
  puVar1 = PTR__ZN8firebase4auth13g_auths_mutexE_00c1bb70;
  uVar5 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c1bb70;
  _ZN8firebase5Mutex7AcquireEv(uVar5);
  uVar7 = *(undefined8 *)puVar1;
  _ZN8firebase5Mutex7AcquireEv(uVar7);
  puVar1 = PTR__ZN8firebase4auth7g_authsE_00c1bb78;
  puVar4 = *(undefined **)(PTR__ZN8firebase4auth7g_authsE_00c1bb78 + 8);
  if (puVar4 != (undefined *)0x0) {
    puVar3 = PTR__ZN8firebase4auth7g_authsE_00c1bb78 + 8;
    do {
                    /* try { // try from 00b5ac18 to 00c5ac5b has its CatchHandler @ 00b5af50 */
      if (*(ulong *)(puVar4 + 0x20) >= param_1) {
        puVar3 = puVar4;
      }
      puVar4 = *(undefined **)(puVar4 + (ulong)(*(ulong *)(puVar4 + 0x20) < param_1) * 8);
    } while (puVar4 != (undefined *)0x0);
    if ((puVar3 != PTR__ZN8firebase4auth7g_authsE_00c1bb78 + 8) &&
       (*(ulong *)(puVar3 + 0x20) <= param_1)) {
      lVar6 = *(long *)(puVar3 + 0x28);
      goto LAB_00b5ac44;
    }
  }
  lVar6 = 0;
LAB_00b5ac44:
  _ZN8firebase5Mutex7ReleaseEv(uVar7);
  if (lVar6 == 0) {
    lVar2 = _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE(param_1);
    if (lVar2 == 0) {
      lVar6 = 0;
    }
    else {
      lVar6 = _Znwm(8);
      _ZN8firebase4auth4AuthC2EPNS_3AppEPv(lVar6,param_1,lVar2);
                    /* try { // try from 00b5acac to 00c5acb7 has its CatchHandler @ 00b5af24 */
      _ZN8firebase8LogDebugEPKcz("Creating Auth %p for App %p",lVar6,param_1);
      puVar10 = (undefined8 *)(puVar1 + 8);
      if ((undefined8 *)*puVar10 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = puVar10;
      }
      else {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = (undefined8 *)(puVar1 + 8);
LAB_00b5acd8:
        do {
          puVar10 = puVar8;
          if ((ulong)puVar10[4] <= param_1) {
            if ((ulong)puVar10[4] < param_1) {
              puVar9 = puVar10 + 1;
              puVar8 = (undefined8 *)*puVar9;
              if ((undefined8 *)*puVar9 != (undefined8 *)0x0) goto LAB_00b5acd8;
            }
            puVar8 = (undefined8 *)*puVar9;
            goto joined_r0x00b5ad40;
          }
          puVar8 = (undefined8 *)*puVar10;
          puVar9 = puVar10;
        } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
        puVar8 = (undefined8 *)*puVar10;
      }
joined_r0x00b5ad40:
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
                    /* try { // try from 00b5ad88 to 00c5ad9b has its CatchHandler @ 00b5aed0 */
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
