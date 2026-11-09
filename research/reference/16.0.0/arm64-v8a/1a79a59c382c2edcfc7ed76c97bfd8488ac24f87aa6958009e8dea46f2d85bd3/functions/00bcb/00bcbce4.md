# 00bcbce4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcbce4",
  "name": "_INIT_290",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "70f5f0aba6fea76c33cc3555caf3ae6f0fe94cb1e7e5f7928edf4eed99919079",
  "source_text_sha256": "70f5f0aba6fea76c33cc3555caf3ae6f0fe94cb1e7e5f7928edf4eed99919079"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a30](../00c57/00c57a30.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c5a7c0](../00c5a/00c5a7c0.md)
- [00c5a880](../00c5a/00c5a880.md)

## 関連文字列（未確認候補）

~~~text
"auth"
~~~

## 疑似コード / UTF-8 940 bytes

~~~c

void _INIT_290(void)

{
  undefined *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  
  DAT_011262e8 = &DAT_002bc0ca;
  DAT_011262f0 = FUN_00bca0a8;
  DAT_011262f8 = FUN_00bca0b0;
  DAT_01126300 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9b5a8;
                    /* try { // try from 00bcbd30 to 00ccbd8f has its CatchHandler @ 00bcbd30
                       catch() { ... } // from try @ 00bcbd30 with catch @ 00bcbd30
                       catch() { ... } // from try @ 00bcbd9c with catch @ 00bcbd30 */
  puVar3 = (undefined8 *)(PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8);
  *puVar3 = 0;
  *(undefined8 *)(puVar1 + 0x10) = 0;
  *(undefined8 **)puVar1 = puVar3;
  __cxa_atexit(FUN_00bca0b4,puVar1,&PTR_LOOP_00c62b90);
  uVar2 = _Znwm(0x28);
  _ZN8firebase5MutexC1ENS0_4ModeE(uVar2,1);
  *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9b5a0 = uVar2;
  return;
}

~~~
