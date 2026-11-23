# 00bbcd3c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbc914`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc914.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0079.md#compare-feabe51bc43a338848683d728e64fe36)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0088.md#compare-3d1a90df260122044b5f3a7087af8a26)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcd3c",
  "name": "_ZN8firebase9messaging18GetTokenLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e2fc3f9cf05b9428e7938da469d2a7a1857f3ad7cdd4f75b7cad540dae43a22",
  "source_text_sha256": "8e2fc3f9cf05b9428e7938da469d2a7a1857f3ad7cdd4f75b7cad540dae43a22"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ad50](../00c5a/00c5ad50.md)
- [00c5ae10](../00c5a/00c5ae10.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5d270](../00c5d/00c5d270.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1070 bytes

~~~c

void _ZN8firebase9messaging18GetTokenLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_01126360 == 0) {
                    /* try { // try from 00bbcda8 to 00cbcdaf has its CatchHandler @ 00bbce7c */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bbcdc4 to 00cbcdcb has its CatchHandler @ 00bbce74 */
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  }
                    /* try { // try from 00bbcddc to 00cbcde3 has its CatchHandler @ 00bbce70 */
  return;
}

~~~
