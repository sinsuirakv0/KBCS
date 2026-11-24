# 00bdaa9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdaa00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0085.md#compare-80136b0fe66f254012d308ae01a71618)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0097.md#compare-70ded1af0a2406fc256b15bd9447b575)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaa9c",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42a6e64f7caf4588f45e8cc16694a9e6c4937499e9b7d92ce0ae99b28d595879",
  "source_text_sha256": "42a6e64f7caf4588f45e8cc16694a9e6c4937499e9b7d92ce0ae99b28d595879"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574d2c](../00574/00574d2c.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b330](../00c5b/00c5b330.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 614 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c9bb10 + 0x10);
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  FUN_00574d2c(plVar2,*(undefined8 *)param_1[1],DAT_01126dc8);
  (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)param_1[1]);
  if ((void *)param_1[1] != (void *)0x0) {
    _ZdlPv((void *)param_1[1]);
    return;
  }
  return;
}

~~~
