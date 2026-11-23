# 00b6babc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6bb84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bb84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0004.md#compare-6425b5871f118e5d25922731dc172a1e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6babc",
  "name": "_ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "189ba4e074b3b982830eff58ff642190835d832c0cfbb03bb8edfd78bffcb496",
  "source_text_sha256": "189ba4e074b3b982830eff58ff642190835d832c0cfbb03bb8edfd78bffcb496",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6babc",
        "00b6bb2f"
      ]
    ],
    "bytes_sha256": "33c6097520bb4cdd6a6435703274dd7c96605ee1dca24d1441ae4dfaa5f6d165",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bde410](../00bde/00bde410.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 873 bytes

~~~c

void _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring
               (undefined8 param_1,undefined8 param_2,long *param_3,undefined8 param_4)

{
  long lVar1;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(local_40,param_1,param_4);
                    /* try { // try from 00b6baf4 to 00c6bb0b has its CatchHandler @ 00b6bcf8 */
  (**(code **)(*param_3 + 0x28))(param_3,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
                    /* try { // try from 00b6bb14 to 00c6bb43 has its CatchHandler @ 00b6bd54 */
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6babc"></a> `00b6babc` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b6bac0"></a> `00b6bac0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6bac4"></a> `00b6bac4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6bac8"></a> `00b6bac8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b6bacc"></a> `00b6bacc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b6bad0"></a> `00b6bad0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b6bad4"></a> `00b6bad4` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00b6bad8"></a> `00b6bad8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b6badc"></a> `00b6badc` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b6bae0"></a> `00b6bae0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b6bae4"></a> `00b6bae4` | `4b ca 01 94` | bl 0x00bde410 | `UNCONDITIONAL_CALL`
<a id="insn-00b6bae8"></a> `00b6bae8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b6baec"></a> `00b6baec` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b6baf0"></a> `00b6baf0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b6baf4"></a> `00b6baf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6baf8"></a> `00b6baf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6bafc"></a> `00b6bafc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b6bb00"></a> `00b6bb00` | `68 00 00 36` | tbz w8,#0x0,0x00b6bb0c | `CONDITIONAL_JUMP`
<a id="insn-00b6bb04"></a> `00b6bb04` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6bb08"></a> `00b6bb08` | `16 bd 01 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b6bb0c"></a> `00b6bb0c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b6bb10"></a> `00b6bb10` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b6bb14"></a> `00b6bb14` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b6bb18"></a> `00b6bb18` | `a1 00 00 54` | b.ne 0x00b6bb2c | `CONDITIONAL_JUMP`
<a id="insn-00b6bb1c"></a> `00b6bb1c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6bb20"></a> `00b6bb20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6bb24"></a> `00b6bb24` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b6bb28"></a> `00b6bb28` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b6bb2c"></a> `00b6bb2c` | `19 bd 01 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6babc`](#insn-00b6babc) 範囲 `[['00b6babc', '00b6baf3']]`
  - `FALL_THROUGH` [`00b6baf0`](#insn-00b6baf0) → [`00b6baf4`](#insn-00b6baf4)
- ブロック [`00b6baf4`](#insn-00b6baf4) 範囲 `[['00b6baf4', '00b6bb03']]`
  - `CONDITIONAL_JUMP` [`00b6bb00`](#insn-00b6bb00) → [`00b6bb0c`](#insn-00b6bb0c)
  - `FALL_THROUGH` [`00b6bb00`](#insn-00b6bb00) → [`00b6bb04`](#insn-00b6bb04)
- ブロック [`00b6bb04`](#insn-00b6bb04) 範囲 `[['00b6bb04', '00b6bb0b']]`
  - `FALL_THROUGH` [`00b6bb08`](#insn-00b6bb08) → [`00b6bb0c`](#insn-00b6bb0c)
- ブロック [`00b6bb0c`](#insn-00b6bb0c) 範囲 `[['00b6bb0c', '00b6bb13']]`
  - `FALL_THROUGH` [`00b6bb10`](#insn-00b6bb10) → [`00b6bb14`](#insn-00b6bb14)
- ブロック [`00b6bb14`](#insn-00b6bb14) 範囲 `[['00b6bb14', '00b6bb1b']]`
  - `CONDITIONAL_JUMP` [`00b6bb18`](#insn-00b6bb18) → [`00b6bb2c`](#insn-00b6bb2c)
  - `FALL_THROUGH` [`00b6bb18`](#insn-00b6bb18) → [`00b6bb1c`](#insn-00b6bb1c)
- ブロック [`00b6bb1c`](#insn-00b6bb1c) 範囲 `[['00b6bb1c', '00b6bb2b']]`
- ブロック [`00b6bb2c`](#insn-00b6bb2c) 範囲 `[['00b6bb2c', '00b6bb2f']]`

## 命令位置別の参照

- [`00b6bac0`](#insn-00b6bac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bac4`](#insn-00b6bac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6badc`](#insn-00b6badc) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bae4`](#insn-00b6bae4) → [`00bde410`](../00bde/00bde410.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde410` · 推定シンボル `None` · 推定型 `None`
- [`00b6bafc`](#insn-00b6bafc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb00`](#insn-00b6bb00) → [`00b6bb0c`](#insn-00b6bb0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb04`](#insn-00b6bb04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb08`](#insn-00b6bb08) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb10`](#insn-00b6bb10) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb18`](#insn-00b6bb18) → [`00b6bb2c`](#insn-00b6bb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb1c`](#insn-00b6bb1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb20`](#insn-00b6bb20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bb2c`](#insn-00b6bb2c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6bac0`](#insn-00b6bac0)

~~~json
{
  "source": "00b6bac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bac4`](#insn-00b6bac4)

~~~json
{
  "source": "00b6bac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6badc`](#insn-00b6badc)

~~~json
{
  "source": "00b6badc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bae4`](#insn-00b6bae4)

~~~json
{
  "source": "00b6bae4",
  "target": "00bde410",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6bafc`](#insn-00b6bafc)

~~~json
{
  "source": "00b6bafc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb00`](#insn-00b6bb00)

~~~json
{
  "source": "00b6bb00",
  "target": "00b6bb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb04`](#insn-00b6bb04)

~~~json
{
  "source": "00b6bb04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb08`](#insn-00b6bb08)

~~~json
{
  "source": "00b6bb08",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6bb10`](#insn-00b6bb10)

~~~json
{
  "source": "00b6bb10",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb18`](#insn-00b6bb18)

~~~json
{
  "source": "00b6bb18",
  "target": "00b6bb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb1c`](#insn-00b6bb1c)

~~~json
{
  "source": "00b6bb1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb20`](#insn-00b6bb20)

~~~json
{
  "source": "00b6bb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bb2c`](#insn-00b6bb2c)

~~~json
{
  "source": "00b6bb2c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
