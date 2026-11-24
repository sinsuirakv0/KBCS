# 00bcf1ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcf1a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf1a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-9ecf0d50d62fa741bbaeff774cf861d4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4bc34`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-a3ba7106efa58b0f1433a948ead2cd27)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcf1ec",
  "name": "FUN_00bcf1ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17b59d3062aff8f6cf15e132823076dbc82d962ff73f13d0288683c51c407e24",
  "source_text_sha256": "17b59d3062aff8f6cf15e132823076dbc82d962ff73f13d0288683c51c407e24",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcf1ec",
        "00bcf2cb"
      ]
    ],
    "bytes_sha256": "6c8983a888c2eae714c801684ce1f7c0e5abeff3b47ac42889357b5968394cd9",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"operator\"\" "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1908 bytes

~~~c

void FUN_00bcf1ec(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 0xbU) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3eb;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
                    /* catch() { ... } // from try @ 00bcf01c with catch @ 00bcf248 */
                    /* catch() { ... } // from try @ 00bcf00c with catch @ 00bcf24c */
  pcVar2 = (char *)((long)__ptr + lVar3);
                    /* catch() { ... } // from try @ 00bcf000 with catch @ 00bcf250 */
                    /* catch() { ... } // from try @ 00bcefc8 with catch @ 00bcf254 */
                    /* catch() { ... } // from try @ 00bceeb0 with catch @ 00bcf258 */
  *(undefined8 *)pcVar2 = s_operator___002ab3aa._0_8_;
  pcVar2[7] = 'r';
  pcVar2[8] = '\"';
  pcVar2[9] = '\"';
  pcVar2[10] = ' ';
  plVar4 = *(long **)(param_1 + 0x10);
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 0xb;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
                    /* catch() { ... } // from try @ 00bceea0 with catch @ 00bcf28c */
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* catch() { ... } // from try @ 00bcee94 with catch @ 00bcf2ac */
                    /* catch() { ... } // from try @ 00bcedd4 with catch @ 00bcf2c0 */
                    /* WARNING: Could not recover jumptable at 0x00bcf2c4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcf1ec"></a> `00bcf1ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcf1f0"></a> `00bcf1f0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcf1f4"></a> `00bcf1f4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf1f8"></a> `00bcf1f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcf1fc"></a> `00bcf1fc` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf200"></a> `00bcf200` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcf204"></a> `00bcf204` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcf208"></a> `00bcf208` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcf20c"></a> `00bcf20c` | `2b 2d 00 91` | add x11,x9,#0xb | `FALL_THROUGH`
<a id="insn-00bcf210"></a> `00bcf210` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcf214"></a> `00bcf214` | `89 01 00 54` | b.ls 0x00bcf244 | `CONDITIONAL_JUMP`
<a id="insn-00bcf218"></a> `00bcf218` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf21c"></a> `00bcf21c` | `29 ad 0f 91` | add x9,x9,#0x3eb | `FALL_THROUGH`
<a id="insn-00bcf220"></a> `00bcf220` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcf224"></a> `00bcf224` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcf228"></a> `00bcf228` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcf22c"></a> `00bcf22c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf230"></a> `00bcf230` | `08 38 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf234"></a> `00bcf234` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcf238"></a> `00bcf238` | `80 04 00 b4` | cbz x0,0x00bcf2c8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf23c"></a> `00bcf23c` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf240"></a> `00bcf240` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcf244"></a> `00bcf244` | `ea b6 ff 90` | adrp x10,0x2ab000 | `FALL_THROUGH`
<a id="insn-00bcf248"></a> `00bcf248` | `4a a9 0e 91` | add x10,x10,#0x3aa | `FALL_THROUGH`
<a id="insn-00bcf24c"></a> `00bcf24c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf250"></a> `00bcf250` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00bcf254"></a> `00bcf254` | `49 4e 84 52` | mov w9,#0x2272 | `FALL_THROUGH`
<a id="insn-00bcf258"></a> `00bcf258` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcf25c"></a> `00bcf25c` | `49 04 a4 72` | movk w9,#0x2022, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcf260"></a> `00bcf260` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcf264"></a> `00bcf264` | `09 71 00 b8` | stur w9,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00bcf268"></a> `00bcf268` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf26c"></a> `00bcf26c` | `94 0a 40 f9` | ldr x20,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf270"></a> `00bcf270` | `08 2d 00 91` | add x8,x8,#0xb | `FALL_THROUGH`
<a id="insn-00bcf274"></a> `00bcf274` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcf278"></a> `00bcf278` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf27c"></a> `00bcf27c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf280"></a> `00bcf280` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf284"></a> `00bcf284` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf288"></a> `00bcf288` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf28c"></a> `00bcf28c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcf290"></a> `00bcf290` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcf294"></a> `00bcf294` | `a1 00 00 54` | b.ne 0x00bcf2a8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf298"></a> `00bcf298` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf29c"></a> `00bcf29c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcf2a0"></a> `00bcf2a0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcf2a4"></a> `00bcf2a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcf2a8"></a> `00bcf2a8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcf2ac"></a> `00bcf2ac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf2b0"></a> `00bcf2b0` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf2b4"></a> `00bcf2b4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcf2b8"></a> `00bcf2b8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf2bc"></a> `00bcf2bc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcf2c0"></a> `00bcf2c0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcf2c4"></a> `00bcf2c4` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcf2c8"></a> `00bcf2c8` | `fe 3b 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcf1ec`](#insn-00bcf1ec) 範囲 `[['00bcf1ec', '00bcf217']]`
  - `CONDITIONAL_JUMP` [`00bcf214`](#insn-00bcf214) → [`00bcf244`](#insn-00bcf244)
  - `FALL_THROUGH` [`00bcf214`](#insn-00bcf214) → [`00bcf218`](#insn-00bcf218)
- ブロック [`00bcf218`](#insn-00bcf218) 範囲 `[['00bcf218', '00bcf23b']]`
  - `CONDITIONAL_JUMP` [`00bcf238`](#insn-00bcf238) → [`00bcf2c8`](#insn-00bcf2c8)
  - `FALL_THROUGH` [`00bcf238`](#insn-00bcf238) → [`00bcf23c`](#insn-00bcf23c)
- ブロック [`00bcf23c`](#insn-00bcf23c) 範囲 `[['00bcf23c', '00bcf243']]`
  - `FALL_THROUGH` [`00bcf240`](#insn-00bcf240) → [`00bcf244`](#insn-00bcf244)
- ブロック [`00bcf244`](#insn-00bcf244) 範囲 `[['00bcf244', '00bcf247']]`
  - `FALL_THROUGH` [`00bcf244`](#insn-00bcf244) → [`00bcf248`](#insn-00bcf248)
- ブロック [`00bcf248`](#insn-00bcf248) 範囲 `[['00bcf248', '00bcf24b']]`
  - `FALL_THROUGH` [`00bcf248`](#insn-00bcf248) → [`00bcf24c`](#insn-00bcf24c)
- ブロック [`00bcf24c`](#insn-00bcf24c) 範囲 `[['00bcf24c', '00bcf24f']]`
  - `FALL_THROUGH` [`00bcf24c`](#insn-00bcf24c) → [`00bcf250`](#insn-00bcf250)
- ブロック [`00bcf250`](#insn-00bcf250) 範囲 `[['00bcf250', '00bcf253']]`
  - `FALL_THROUGH` [`00bcf250`](#insn-00bcf250) → [`00bcf254`](#insn-00bcf254)
- ブロック [`00bcf254`](#insn-00bcf254) 範囲 `[['00bcf254', '00bcf257']]`
  - `FALL_THROUGH` [`00bcf254`](#insn-00bcf254) → [`00bcf258`](#insn-00bcf258)
- ブロック [`00bcf258`](#insn-00bcf258) 範囲 `[['00bcf258', '00bcf28b']]`
  - `FALL_THROUGH` [`00bcf288`](#insn-00bcf288) → [`00bcf28c`](#insn-00bcf28c)
- ブロック [`00bcf28c`](#insn-00bcf28c) 範囲 `[['00bcf28c', '00bcf297']]`
  - `CONDITIONAL_JUMP` [`00bcf294`](#insn-00bcf294) → [`00bcf2a8`](#insn-00bcf2a8)
  - `FALL_THROUGH` [`00bcf294`](#insn-00bcf294) → [`00bcf298`](#insn-00bcf298)
- ブロック [`00bcf298`](#insn-00bcf298) 範囲 `[['00bcf298', '00bcf2a7']]`
- ブロック [`00bcf2a8`](#insn-00bcf2a8) 範囲 `[['00bcf2a8', '00bcf2ab']]`
  - `FALL_THROUGH` [`00bcf2a8`](#insn-00bcf2a8) → [`00bcf2ac`](#insn-00bcf2ac)
- ブロック [`00bcf2ac`](#insn-00bcf2ac) 範囲 `[['00bcf2ac', '00bcf2bf']]`
  - `FALL_THROUGH` [`00bcf2bc`](#insn-00bcf2bc) → [`00bcf2c0`](#insn-00bcf2c0)
- ブロック [`00bcf2c0`](#insn-00bcf2c0) 範囲 `[['00bcf2c0', '00bcf2c7']]`
- ブロック [`00bcf2c8`](#insn-00bcf2c8) 範囲 `[['00bcf2c8', '00bcf2cb']]`

## 命令位置別の参照

- [`00bcf1f0`](#insn-00bcf1f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf1f4`](#insn-00bcf1f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf214`](#insn-00bcf214) → [`00bcf244`](#insn-00bcf244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf230`](#insn-00bcf230) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcf238`](#insn-00bcf238) → [`00bcf2c8`](#insn-00bcf2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf250`](#insn-00bcf250) → `002ab3aa`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf294`](#insn-00bcf294) → [`00bcf2a8`](#insn-00bcf2a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf298`](#insn-00bcf298) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf29c`](#insn-00bcf29c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2b8`](#insn-00bcf2b8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2bc`](#insn-00bcf2bc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf2c8`](#insn-00bcf2c8) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcf1f0`](#insn-00bcf1f0)

~~~json
{
  "source": "00bcf1f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf1f4`](#insn-00bcf1f4)

~~~json
{
  "source": "00bcf1f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf214`](#insn-00bcf214)

~~~json
{
  "source": "00bcf214",
  "target": "00bcf244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf230`](#insn-00bcf230)

~~~json
{
  "source": "00bcf230",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf238`](#insn-00bcf238)

~~~json
{
  "source": "00bcf238",
  "target": "00bcf2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf250`](#insn-00bcf250)

~~~json
{
  "source": "00bcf250",
  "target": "002ab3aa",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab3aa",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "6f70657261746f7222222000",
  "capture_start": "002ab3aa",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf294`](#insn-00bcf294)

~~~json
{
  "source": "00bcf294",
  "target": "00bcf2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf298`](#insn-00bcf298)

~~~json
{
  "source": "00bcf298",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf29c`](#insn-00bcf29c)

~~~json
{
  "source": "00bcf29c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2b8`](#insn-00bcf2b8)

~~~json
{
  "source": "00bcf2b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2bc`](#insn-00bcf2bc)

~~~json
{
  "source": "00bcf2bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf2c8`](#insn-00bcf2c8)

~~~json
{
  "source": "00bcf2c8",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
