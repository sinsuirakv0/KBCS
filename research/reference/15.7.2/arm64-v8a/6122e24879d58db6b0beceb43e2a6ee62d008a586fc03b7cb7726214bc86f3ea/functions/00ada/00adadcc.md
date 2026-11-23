# 00adadcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adae94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-97186c7e1a72215b36f03e48abad049b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adadcc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementContentReady",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad329a4145b72e5f9deef805996008d199fac90cf2a9f34f8792b8e64a26d943",
  "source_text_sha256": "ad329a4145b72e5f9deef805996008d199fac90cf2a9f34f8792b8e64a26d943",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adadcc",
        "00adae5b"
      ],
      [
        "00adae88",
        "00adae8b"
      ]
    ],
    "bytes_sha256": "b8298101d0405cad58bd5d012ed8caa6931f3e787cd91d1839aa1eef99b8e743",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adb914](../00adb/00adb914.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 880 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementContentReady
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adb914(&DAT_0109fe38,local_40);
  if ((puVar2 != &DAT_0109fe40) && (plVar3 = (long *)puVar2[0x18], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
                    /* catch() { ... } // from try @ 00adae80 with catch @ 00adae50 */
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
<a id="insn-00adadcc"></a> `00adadcc` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adadd0"></a> `00adadd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adadd4"></a> `00adadd4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adadd8"></a> `00adadd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adaddc"></a> `00adaddc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adade0"></a> `00adade0` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adade4"></a> `00adade4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adade8"></a> `00adade8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adadec"></a> `00adadec` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00adadf0"></a> `00adadf0` | `23 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adadf4"></a> `00adadf4` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adadf8"></a> `00adadf8` | `00 e0 38 91` | add x0,x0,#0xe38 | `FALL_THROUGH`
<a id="insn-00adadfc"></a> `00adadfc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adae00"></a> `00adae00` | `c5 02 00 94` | bl 0x00adb914 | `UNCONDITIONAL_CALL`
<a id="insn-00adae04"></a> `00adae04` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adae08"></a> `00adae08` | `08 01 39 91` | add x8,x8,#0xe40 | `FALL_THROUGH`
<a id="insn-00adae0c"></a> `00adae0c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adae10"></a> `00adae10` | `e0 00 00 54` | b.eq 0x00adae2c | `CONDITIONAL_JUMP`
<a id="insn-00adae14"></a> `00adae14` | `00 60 40 f9` | ldr x0,[x0, #0xc0] | `FALL_THROUGH`
<a id="insn-00adae18"></a> `00adae18` | `a0 00 00 b4` | cbz x0,0x00adae2c | `CONDITIONAL_JUMP`
<a id="insn-00adae1c"></a> `00adae1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adae20"></a> `00adae20` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adae24"></a> `00adae24` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adae28"></a> `00adae28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adae2c"></a> `00adae2c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00adae30"></a> `00adae30` | `68 00 00 36` | tbz w8,#0x0,0x00adae3c | `CONDITIONAL_JUMP`
<a id="insn-00adae34"></a> `00adae34` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adae38"></a> `00adae38` | `4a 00 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adae3c"></a> `00adae3c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adae40"></a> `00adae40` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adae44"></a> `00adae44` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adae48"></a> `00adae48` | `01 02 00 54` | b.ne 0x00adae88 | `CONDITIONAL_JUMP`
<a id="insn-00adae4c"></a> `00adae4c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adae50"></a> `00adae50` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adae54"></a> `00adae54` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adae58"></a> `00adae58` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adae88"></a> `00adae88` | `42 00 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adadcc`](#insn-00adadcc) 範囲 `[['00adadcc', '00adae13']]`
  - `CONDITIONAL_JUMP` [`00adae10`](#insn-00adae10) → [`00adae2c`](#insn-00adae2c)
  - `FALL_THROUGH` [`00adae10`](#insn-00adae10) → [`00adae14`](#insn-00adae14)
- ブロック [`00adae14`](#insn-00adae14) 範囲 `[['00adae14', '00adae1b']]`
  - `CONDITIONAL_JUMP` [`00adae18`](#insn-00adae18) → [`00adae2c`](#insn-00adae2c)
  - `FALL_THROUGH` [`00adae18`](#insn-00adae18) → [`00adae1c`](#insn-00adae1c)
- ブロック [`00adae1c`](#insn-00adae1c) 範囲 `[['00adae1c', '00adae2b']]`
  - `FALL_THROUGH` [`00adae28`](#insn-00adae28) → [`00adae2c`](#insn-00adae2c)
- ブロック [`00adae2c`](#insn-00adae2c) 範囲 `[['00adae2c', '00adae33']]`
  - `CONDITIONAL_JUMP` [`00adae30`](#insn-00adae30) → [`00adae3c`](#insn-00adae3c)
  - `FALL_THROUGH` [`00adae30`](#insn-00adae30) → [`00adae34`](#insn-00adae34)
- ブロック [`00adae34`](#insn-00adae34) 範囲 `[['00adae34', '00adae3b']]`
  - `FALL_THROUGH` [`00adae38`](#insn-00adae38) → [`00adae3c`](#insn-00adae3c)
- ブロック [`00adae3c`](#insn-00adae3c) 範囲 `[['00adae3c', '00adae4b']]`
  - `CONDITIONAL_JUMP` [`00adae48`](#insn-00adae48) → [`00adae88`](#insn-00adae88)
  - `FALL_THROUGH` [`00adae48`](#insn-00adae48) → [`00adae4c`](#insn-00adae4c)
- ブロック [`00adae4c`](#insn-00adae4c) 範囲 `[['00adae4c', '00adae4f']]`
  - `FALL_THROUGH` [`00adae4c`](#insn-00adae4c) → [`00adae50`](#insn-00adae50)
- ブロック [`00adae50`](#insn-00adae50) 範囲 `[['00adae50', '00adae5b']]`
- ブロック [`00adae88`](#insn-00adae88) 範囲 `[['00adae88', '00adae8b']]`

## 命令位置別の参照

- [`00adadd0`](#insn-00adadd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadd4`](#insn-00adadd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adade8`](#insn-00adade8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadf0`](#insn-00adadf0) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adadf8`](#insn-00adadf8) → `0109fe38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adae00`](#insn-00adae00) → [`00adb914`](../00adb/00adb914.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb914` · 推定シンボル `None` · 推定型 `None`
- [`00adae10`](#insn-00adae10) → [`00adae2c`](#insn-00adae2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae18`](#insn-00adae18) → [`00adae2c`](#insn-00adae2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae2c`](#insn-00adae2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae30`](#insn-00adae30) → [`00adae3c`](#insn-00adae3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae34`](#insn-00adae34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae38`](#insn-00adae38) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adae40`](#insn-00adae40) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae48`](#insn-00adae48) → [`00adae88`](#insn-00adae88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae4c`](#insn-00adae4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae50`](#insn-00adae50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae88`](#insn-00adae88) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adadd0`](#insn-00adadd0)

~~~json
{
  "source": "00adadd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadd4`](#insn-00adadd4)

~~~json
{
  "source": "00adadd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adade8`](#insn-00adade8)

~~~json
{
  "source": "00adade8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadf0`](#insn-00adadf0)

~~~json
{
  "source": "00adadf0",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adadf8`](#insn-00adadf8)

~~~json
{
  "source": "00adadf8",
  "target": "0109fe38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adae00`](#insn-00adae00)

~~~json
{
  "source": "00adae00",
  "target": "00adb914",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae10`](#insn-00adae10)

~~~json
{
  "source": "00adae10",
  "target": "00adae2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae18`](#insn-00adae18)

~~~json
{
  "source": "00adae18",
  "target": "00adae2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae2c`](#insn-00adae2c)

~~~json
{
  "source": "00adae2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae30`](#insn-00adae30)

~~~json
{
  "source": "00adae30",
  "target": "00adae3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae34`](#insn-00adae34)

~~~json
{
  "source": "00adae34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae38`](#insn-00adae38)

~~~json
{
  "source": "00adae38",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae40`](#insn-00adae40)

~~~json
{
  "source": "00adae40",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae48`](#insn-00adae48)

~~~json
{
  "source": "00adae48",
  "target": "00adae88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae4c`](#insn-00adae4c)

~~~json
{
  "source": "00adae4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae50`](#insn-00adae50)

~~~json
{
  "source": "00adae50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae88`](#insn-00adae88)

~~~json
{
  "source": "00adae88",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
