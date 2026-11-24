# 00baecc4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baec80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baec80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-9a631378855808fdf319a89a83878455)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2b70c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b70c.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-35cc7679ab2f96e05eff4406f6371089)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baecc4",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0467b6cbcc7e0681d091abd551204a84a34ff82efc05dd54a2d4171d773baaaf",
  "source_text_sha256": "0467b6cbcc7e0681d091abd551204a84a34ff82efc05dd54a2d4171d773baaaf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baecc4",
        "00baed33"
      ]
    ],
    "bytes_sha256": "f254ef795e09a122ffd70de474e7c49f7e6466524f41fbd08cb55af7c2e1987a",
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

- [00babe6c](../00bab/00babe6c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 768 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* try { // try from 00baece4 to 00caecef has its CatchHandler @ 00baee78 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00baed08 to 00caed0f has its CatchHandler @ 00baee64 */
  FUN_00babe6c(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baecc4"></a> `00baecc4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baecc8"></a> `00baecc8` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baeccc"></a> `00baeccc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baecd0"></a> `00baecd0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baecd4"></a> `00baecd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baecd8"></a> `00baecd8` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baecdc"></a> `00baecdc` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00baece0"></a> `00baece0` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baece4"></a> `00baece4` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00baece8"></a> `00baece8` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baecec"></a> `00baecec` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baecf0"></a> `00baecf0` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baecf4"></a> `00baecf4` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baecf8"></a> `00baecf8` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baecfc"></a> `00baecfc` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baed00"></a> `00baed00` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baed04"></a> `00baed04` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00baed08"></a> `00baed08` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baed0c"></a> `00baed0c` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00baed10"></a> `00baed10` | `57 f4 ff 97` | bl 0x00babe6c | `UNCONDITIONAL_CALL`
<a id="insn-00baed14"></a> `00baed14` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baed18"></a> `00baed18` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baed1c"></a> `00baed1c` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baed20"></a> `00baed20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed24"></a> `00baed24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baed28"></a> `00baed28` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baed2c"></a> `00baed2c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baed30"></a> `00baed30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baecc4`](#insn-00baecc4) 範囲 `[['00baecc4', '00baece3']]`
  - `FALL_THROUGH` [`00baece0`](#insn-00baece0) → [`00baece4`](#insn-00baece4)
- ブロック [`00baece4`](#insn-00baece4) 範囲 `[['00baece4', '00baed07']]`
  - `FALL_THROUGH` [`00baed04`](#insn-00baed04) → [`00baed08`](#insn-00baed08)
- ブロック [`00baed08`](#insn-00baed08) 範囲 `[['00baed08', '00baed33']]`

## 命令位置別の参照

- [`00baeccc`](#insn-00baeccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecd0`](#insn-00baecd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecf8`](#insn-00baecf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed10`](#insn-00baed10) → [`00babe6c`](../00bab/00babe6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00babe6c` · 推定シンボル `None` · 推定型 `None`
- [`00baed14`](#insn-00baed14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed20`](#insn-00baed20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed24`](#insn-00baed24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeccc`](#insn-00baeccc)

~~~json
{
  "source": "00baeccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecd0`](#insn-00baecd0)

~~~json
{
  "source": "00baecd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecf8`](#insn-00baecf8)

~~~json
{
  "source": "00baecf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed10`](#insn-00baed10)

~~~json
{
  "source": "00baed10",
  "target": "00babe6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baed14`](#insn-00baed14)

~~~json
{
  "source": "00baed14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed20`](#insn-00baed20)

~~~json
{
  "source": "00baed20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed24`](#insn-00baed24)

~~~json
{
  "source": "00baed24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
