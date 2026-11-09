# 00bcaec8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcaec8",
  "name": "_ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90474be1b35e84cc64e2e4f6f5104a10d80b01d067c9399e3ff2510510fc3f77",
  "source_text_sha256": "90474be1b35e84cc64e2e4f6f5104a10d80b01d067c9399e3ff2510510fc3f77"
}
~~~

## 呼び出し元

- [00c5d660](../00c5d/00c5d660.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5d600](../00c5d/00c5d600.md)

## 疑似コード / UTF-8 3383 bytes

~~~c

void _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE
               (long *param_1,long param_2)

{
  long *plVar1;
  undefined8 *puVar2;
  long *plVar3;
  undefined8 *puVar4;
  long *plVar5;
  undefined8 *puVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  
                    /* try { // try from 00bcaed0 to 00ccaedb has its CatchHandler @ 00bcafd0 */
                    /* try { // try from 00bcaedc to 00ccaeff has its CatchHandler @ 00bcae6c */
  lVar9 = *param_1;
  if (lVar9 != 0) {
    lVar7 = *(long *)(lVar9 + 0x250);
    lVar8 = *(long *)(lVar9 + 0x248);
    _ZN8firebase5Mutex7AcquireEv(lVar9 + 0x268);
                    /* try { // try from 00bcaf00 to 00ccaf0b has its CatchHandler @ 00bcafd0 */
    plVar5 = *(long **)(lVar9 + 0x248);
    plVar3 = *(long **)(lVar9 + 0x250);
                    /* try { // try from 00bcaf0c to 00ccaf33 has its CatchHandler @ 00bcae6c */
    if (plVar3 != plVar5) {
      if (*plVar5 != param_2) {
        do {
          if (plVar3 + -1 == plVar5) goto LAB_00bcaf68;
          plVar1 = plVar5 + 1;
          plVar5 = plVar5 + 1;
                    /* try { // try from 00bcaf34 to 00ccaf3f has its CatchHandler @ 00bcafd0 */
        } while (*plVar1 != param_2);
      }
                    /* try { // try from 00bcaf40 to 00ccaf5f has its CatchHandler @ 00bcae6c */
      if (plVar5 != plVar3) {
        if (plVar3 + -1 != plVar5) {
          *plVar5 = plVar3[-1];
          plVar3 = *(long **)(lVar9 + 0x250);
        }
                    /* try { // try from 00bcaf60 to 00ccaf67 has its CatchHandler @ 00bcafd0 */
        *(long **)(lVar9 + 0x250) = plVar3 + -1;
      }
    }
LAB_00bcaf68:
                    /* try { // try from 00bcaf68 to 00ccaf87 has its CatchHandler @ 00bcae6c */
    puVar6 = *(undefined8 **)(param_2 + 8);
    puVar4 = *(undefined8 **)(param_2 + 0x10);
    if (puVar4 != puVar6) {
      if ((long *)*puVar6 != param_1) {
        do {
                    /* try { // try from 00bcaf88 to 00ccaf93 has its CatchHandler @ 00bcafd0 */
          if (puVar4 + -1 == puVar6) goto LAB_00bcafcc;
          puVar2 = puVar6 + 1;
                    /* try { // try from 00bcaf94 to 00ccafd3 has its CatchHandler @ 00bcae6c */
          puVar6 = puVar6 + 1;
        } while ((long *)*puVar2 != param_1);
      }
      if (puVar6 != puVar4) {
        if (puVar4 + -1 != puVar6) {
          *puVar6 = puVar4[-1];
          puVar4 = *(undefined8 **)(param_2 + 0x10);
        }
        *(undefined8 **)(param_2 + 0x10) = puVar4 + -1;
      }
    }
LAB_00bcafcc:
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bcaed0 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf00 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf34 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf60 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf88 with catch @ 00bcafd0
                        */
    _ZN8firebase5Mutex7ReleaseEv(lVar9 + 0x268);
    if ((ulong)(*(long *)(*param_1 + 0x250) - *(long *)(*param_1 + 0x248) >> 3) <
        (ulong)(long)(int)((ulong)(lVar7 - lVar8) >> 3)) {
      _ZN8firebase4auth23DisableTokenAutoRefreshEPNS0_8AuthDataE();
      return;
    }
  }
  return;
}

~~~
