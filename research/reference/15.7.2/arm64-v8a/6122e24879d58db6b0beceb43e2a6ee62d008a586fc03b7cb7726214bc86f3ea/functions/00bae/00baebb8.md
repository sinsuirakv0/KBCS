# 00baebb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baec80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baec80.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-51ad2266b2326229580058ac55568558)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baebb8",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0632f2bdfd414c6a4a1997ba12dc312c6d77812b1583e567044225620d54d960",
  "source_text_sha256": "0632f2bdfd414c6a4a1997ba12dc312c6d77812b1583e567044225620d54d960",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baebb8",
        "00baec27"
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

- [00babd60](../00bab/00babd60.md)

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
  
                    /* try { // try from 00baebd8 to 00caebe3 has its CatchHandler @ 00baed6c */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00baebfc to 00caec03 has its CatchHandler @ 00baed58 */
  FUN_00babd60(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
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
<a id="insn-00baebb8"></a> `00baebb8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baebbc"></a> `00baebbc` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baebc0"></a> `00baebc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baebc4"></a> `00baebc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baebc8"></a> `00baebc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baebcc"></a> `00baebcc` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baebd0"></a> `00baebd0` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00baebd4"></a> `00baebd4` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baebd8"></a> `00baebd8` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00baebdc"></a> `00baebdc` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baebe0"></a> `00baebe0` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baebe4"></a> `00baebe4` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baebe8"></a> `00baebe8` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baebec"></a> `00baebec` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baebf0"></a> `00baebf0` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baebf4"></a> `00baebf4` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baebf8"></a> `00baebf8` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00baebfc"></a> `00baebfc` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baec00"></a> `00baec00` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00baec04"></a> `00baec04` | `57 f4 ff 97` | bl 0x00babd60 | `UNCONDITIONAL_CALL`
<a id="insn-00baec08"></a> `00baec08` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baec0c"></a> `00baec0c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baec10"></a> `00baec10` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baec14"></a> `00baec14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baec18"></a> `00baec18` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baec1c"></a> `00baec1c` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baec20"></a> `00baec20` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baec24"></a> `00baec24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baebb8`](#insn-00baebb8) 範囲 `[['00baebb8', '00baebd7']]`
  - `FALL_THROUGH` [`00baebd4`](#insn-00baebd4) → [`00baebd8`](#insn-00baebd8)
- ブロック [`00baebd8`](#insn-00baebd8) 範囲 `[['00baebd8', '00baebfb']]`
  - `FALL_THROUGH` [`00baebf8`](#insn-00baebf8) → [`00baebfc`](#insn-00baebfc)
- ブロック [`00baebfc`](#insn-00baebfc) 範囲 `[['00baebfc', '00baec27']]`

## 命令位置別の参照

- [`00baebc0`](#insn-00baebc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebc4`](#insn-00baebc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebec`](#insn-00baebec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec04`](#insn-00baec04) → [`00babd60`](../00bab/00babd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00babd60` · 推定シンボル `None` · 推定型 `None`
- [`00baec08`](#insn-00baec08) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec14`](#insn-00baec14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec18`](#insn-00baec18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baebc0`](#insn-00baebc0)

~~~json
{
  "source": "00baebc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebc4`](#insn-00baebc4)

~~~json
{
  "source": "00baebc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebec`](#insn-00baebec)

~~~json
{
  "source": "00baebec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec04`](#insn-00baec04)

~~~json
{
  "source": "00baec04",
  "target": "00babd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baec08`](#insn-00baec08)

~~~json
{
  "source": "00baec08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec14`](#insn-00baec14)

~~~json
{
  "source": "00baec14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec18`](#insn-00baec18)

~~~json
{
  "source": "00baec18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
