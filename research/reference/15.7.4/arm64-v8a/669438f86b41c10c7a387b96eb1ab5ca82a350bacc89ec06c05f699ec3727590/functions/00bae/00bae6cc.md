# 00bae6cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bae688`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae688.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-cba090750b98e8291bdd1461b0d050e1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2b114`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b114.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-7ce3e1b7a5383422eec3558244fdbccd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bae6cc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26b4bf1e3e92f277b43a34aac4ab2869f8de2fe60311d0e8b75d2d5a115bc0c2",
  "source_text_sha256": "26b4bf1e3e92f277b43a34aac4ab2869f8de2fe60311d0e8b75d2d5a115bc0c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bae6cc",
        "00bae73b"
      ]
    ],
    "bytes_sha256": "5ac888eebe71f3e2bf1e7873a74845663dfd04db29bed94b9931a0ad0c02beb2",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae73c](../00bae/00bae73c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 659 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00bae8c8 with catch @ 00bae6ec */
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bae73c(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x18),
               *(undefined4 *)(param_1 + 0x20));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bae6cc"></a> `00bae6cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bae6d0"></a> `00bae6d0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bae6d4"></a> `00bae6d4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae6d8"></a> `00bae6d8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae6dc"></a> `00bae6dc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bae6e0"></a> `00bae6e0` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00bae6e4"></a> `00bae6e4` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00bae6e8"></a> `00bae6e8` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00bae6ec"></a> `00bae6ec` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00bae6f0"></a> `00bae6f0` | `06 0c 40 f9` | ldr x6,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bae6f4"></a> `00bae6f4` | `07 20 40 b9` | ldr w7,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bae6f8"></a> `00bae6f8` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00bae6fc"></a> `00bae6fc` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00bae700"></a> `00bae700` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00bae704"></a> `00bae704` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bae708"></a> `00bae708` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00bae70c"></a> `00bae70c` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00bae710"></a> `00bae710` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00bae714"></a> `00bae714` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00bae718"></a> `00bae718` | `09 00 00 94` | bl 0x00bae73c | `UNCONDITIONAL_CALL`
<a id="insn-00bae71c"></a> `00bae71c` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00bae720"></a> `00bae720` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bae724"></a> `00bae724` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bae728"></a> `00bae728` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae72c"></a> `00bae72c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae730"></a> `00bae730` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bae734"></a> `00bae734` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bae738"></a> `00bae738` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bae6cc`](#insn-00bae6cc) 範囲 `[['00bae6cc', '00bae6eb']]`
  - `FALL_THROUGH` [`00bae6e8`](#insn-00bae6e8) → [`00bae6ec`](#insn-00bae6ec)
- ブロック [`00bae6ec`](#insn-00bae6ec) 範囲 `[['00bae6ec', '00bae73b']]`

## 命令位置別の参照

- [`00bae6d4`](#insn-00bae6d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae6d8`](#insn-00bae6d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae700`](#insn-00bae700) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae718`](#insn-00bae718) → [`00bae73c`](00bae73c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bae73c` · 推定シンボル `None` · 推定型 `None`
- [`00bae71c`](#insn-00bae71c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae728`](#insn-00bae728) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae72c`](#insn-00bae72c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bae6d4`](#insn-00bae6d4)

~~~json
{
  "source": "00bae6d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae6d8`](#insn-00bae6d8)

~~~json
{
  "source": "00bae6d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae700`](#insn-00bae700)

~~~json
{
  "source": "00bae700",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae718`](#insn-00bae718)

~~~json
{
  "source": "00bae718",
  "target": "00bae73c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bae71c`](#insn-00bae71c)

~~~json
{
  "source": "00bae71c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae728`](#insn-00bae728)

~~~json
{
  "source": "00bae728",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae72c`](#insn-00bae72c)

~~~json
{
  "source": "00bae72c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
