# 00baed6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baee34`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baee34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-ccb61dcffe4ee830b1d280bd467a4d00)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baed6c",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa022cd3e817c298bfd85da7a64aeafe8dca7f13f9e426555061545f1e90e56e",
  "source_text_sha256": "aa022cd3e817c298bfd85da7a64aeafe8dca7f13f9e426555061545f1e90e56e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baed6c",
        "00baeddb"
      ]
    ],
    "bytes_sha256": "1d1458aad514a5207ea53eb1e36805535b4733d3fa210ffe609fdca3a59e0ba8",
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

- [00bae8c8](../00bae/00bae8c8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 834 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00baeb68 with catch @ 00baed7c */
                    /* catch() { ... } // from try @ 00baeb34 with catch @ 00baed90 */
                    /* catch() { ... } // from try @ 00baeb74 with catch @ 00baed98 */
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bae8c8(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
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
<a id="insn-00baed6c"></a> `00baed6c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baed70"></a> `00baed70` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baed74"></a> `00baed74` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baed78"></a> `00baed78` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed7c"></a> `00baed7c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baed80"></a> `00baed80` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baed84"></a> `00baed84` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00baed88"></a> `00baed88` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baed8c"></a> `00baed8c` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00baed90"></a> `00baed90` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baed94"></a> `00baed94` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baed98"></a> `00baed98` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baed9c"></a> `00baed9c` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baeda0"></a> `00baeda0` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baeda4"></a> `00baeda4` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baeda8"></a> `00baeda8` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baedac"></a> `00baedac` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00baedb0"></a> `00baedb0` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baedb4"></a> `00baedb4` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00baedb8"></a> `00baedb8` | `c4 fe ff 97` | bl 0x00bae8c8 | `UNCONDITIONAL_CALL`
<a id="insn-00baedbc"></a> `00baedbc` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baedc0"></a> `00baedc0` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baedc4"></a> `00baedc4` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baedc8"></a> `00baedc8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baedcc"></a> `00baedcc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baedd0"></a> `00baedd0` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baedd4"></a> `00baedd4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baedd8"></a> `00baedd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baed6c`](#insn-00baed6c) 範囲 `[['00baed6c', '00baed7b']]`
  - `FALL_THROUGH` [`00baed78`](#insn-00baed78) → [`00baed7c`](#insn-00baed7c)
- ブロック [`00baed7c`](#insn-00baed7c) 範囲 `[['00baed7c', '00baed8f']]`
  - `FALL_THROUGH` [`00baed8c`](#insn-00baed8c) → [`00baed90`](#insn-00baed90)
- ブロック [`00baed90`](#insn-00baed90) 範囲 `[['00baed90', '00baed97']]`
  - `FALL_THROUGH` [`00baed94`](#insn-00baed94) → [`00baed98`](#insn-00baed98)
- ブロック [`00baed98`](#insn-00baed98) 範囲 `[['00baed98', '00baeddb']]`

## 命令位置別の参照

- [`00baed74`](#insn-00baed74) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed78`](#insn-00baed78) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeda0`](#insn-00baeda0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedb8`](#insn-00baedb8) → [`00bae8c8`](00bae8c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bae8c8` · 推定シンボル `None` · 推定型 `None`
- [`00baedbc`](#insn-00baedbc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedc8`](#insn-00baedc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedcc`](#insn-00baedcc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baed74`](#insn-00baed74)

~~~json
{
  "source": "00baed74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed78`](#insn-00baed78)

~~~json
{
  "source": "00baed78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeda0`](#insn-00baeda0)

~~~json
{
  "source": "00baeda0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedb8`](#insn-00baedb8)

~~~json
{
  "source": "00baedb8",
  "target": "00bae8c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baedbc`](#insn-00baedbc)

~~~json
{
  "source": "00baedbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedc8`](#insn-00baedc8)

~~~json
{
  "source": "00baedc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedcc`](#insn-00baedcc)

~~~json
{
  "source": "00baedcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
