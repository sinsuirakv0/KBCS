# 00bba8ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bba8a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-8c68c0bdfaca03d78c29ea18673b32e6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37334`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-21fc96b3b9d76800a2b798ad5f9090c7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba8ec",
  "name": "__cxa_guard_abort",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "544ae8e0fab000b7dda7d4ac760ffbb2625bf40ab7a31884540f1271ca9e2787",
  "source_text_sha256": "544ae8e0fab000b7dda7d4ac760ffbb2625bf40ab7a31884540f1271ca9e2787",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba8ec",
        "00bba983"
      ]
    ],
    "bytes_sha256": "5ca273baaec75a3a6aa6511a7fc2328fe99ed45d5b9ce756ba136dd0b0cc0218",
    "instruction_count": 38,
    "instruction_bytes": 152,
    "body_bytes": 152,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb140](../00bdb/00bdb140.md)

## 呼び出し先

- [00bbb19c](../00bbb/00bbb19c.md)
- [00bde820](../00bde/00bde820.md)
- [00bde830](../00bde/00bde830.md)
- [00be11c0](../00be1/00be11c0.md)

## 関連文字列（未確認候補）

~~~text
"%s failed to acquire mutex"
"%s failed to broadcast"
"%s failed to release mutex"
"__cxa_guard_abort"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1558 bytes

~~~c

void __cxa_guard_abort(long param_1)

{
  byte bVar1;
  int iVar2;
  char *pcVar3;
  
                    /* catch() { ... } // from try @ 00bb50a0 with catch @ 00bba8f0 */
                    /* catch() { ... } // from try @ 00bb4cdc with catch @ 00bba8f4 */
  iVar2 = pthread_mutex_lock((pthread_mutex_t *)&DAT_010a3700);
  if (iVar2 == 0) {
    bVar1 = *(byte *)(param_1 + 1);
    *(undefined4 *)(param_1 + 4) = 0;
    *(undefined1 *)(param_1 + 1) = 0;
                    /* catch() { ... } // from try @ 00bb4ccc with catch @ 00bba920 */
    iVar2 = pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a3700);
    if (iVar2 != 0) {
                    /* catch() { ... } // from try @ 00bb48ec with catch @ 00bba964 */
                    /* WARNING: Subroutine does not return */
      FUN_00bbb19c("%s failed to release mutex","__cxa_guard_abort");
    }
                    /* catch() { ... } // from try @ 00bb4cc0 with catch @ 00bba934 */
                    /* catch() { ... } // from try @ 00bb48fc with catch @ 00bba938 */
    if (((bVar1 >> 2 & 1) == 0) ||
       (iVar2 = pthread_cond_broadcast((pthread_cond_t *)&DAT_010a3728), iVar2 == 0)) {
      return;
    }
    pcVar3 = "%s failed to broadcast";
  }
  else {
    pcVar3 = "%s failed to acquire mutex";
  }
                    /* catch() { ... } // from try @ 00bb48e0 with catch @ 00bba978 */
                    /* catch() { ... } // from try @ 00bb453c with catch @ 00bba97c */
                    /* WARNING: Subroutine does not return */
  FUN_00bbb19c(pcVar3,"__cxa_guard_abort");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba8ec"></a> `00bba8ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bba8f0"></a> `00bba8f0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bba8f4"></a> `00bba8f4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba8f8"></a> `00bba8f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bba8fc"></a> `00bba8fc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bba900"></a> `00bba900` | `40 27 00 b0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba904"></a> `00bba904` | `00 00 1c 91` | add x0,x0,#0x700 | `FALL_THROUGH`
<a id="insn-00bba908"></a> `00bba908` | `c6 8f 00 94` | bl 0x00bde820 | `UNCONDITIONAL_CALL`
<a id="insn-00bba90c"></a> `00bba90c` | `20 02 00 35` | cbnz w0,0x00bba950 | `CONDITIONAL_JUMP`
<a id="insn-00bba910"></a> `00bba910` | `74 06 40 39` | ldrb w20,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bba914"></a> `00bba914` | `7f 06 00 b9` | str wzr,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00bba918"></a> `00bba918` | `7f 06 00 39` | strb wzr,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bba91c"></a> `00bba91c` | `40 27 00 b0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba920"></a> `00bba920` | `00 00 1c 91` | add x0,x0,#0x700 | `FALL_THROUGH`
<a id="insn-00bba924"></a> `00bba924` | `c3 8f 00 94` | bl 0x00bde830 | `UNCONDITIONAL_CALL`
<a id="insn-00bba928"></a> `00bba928` | `a0 01 00 35` | cbnz w0,0x00bba95c | `CONDITIONAL_JUMP`
<a id="insn-00bba92c"></a> `00bba92c` | `b4 00 10 36` | tbz w20,#0x2,0x00bba940 | `CONDITIONAL_JUMP`
<a id="insn-00bba930"></a> `00bba930` | `40 27 00 b0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba934"></a> `00bba934` | `00 a0 1c 91` | add x0,x0,#0x728 | `FALL_THROUGH`
<a id="insn-00bba938"></a> `00bba938` | `22 9a 00 94` | bl 0x00be11c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba93c"></a> `00bba93c` | `a0 01 00 35` | cbnz w0,0x00bba970 | `CONDITIONAL_JUMP`
<a id="insn-00bba940"></a> `00bba940` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba944"></a> `00bba944` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bba948"></a> `00bba948` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bba94c"></a> `00bba94c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bba950"></a> `00bba950` | `e0 b6 ff 90` | adrp x0,0x296000 | `FALL_THROUGH`
<a id="insn-00bba954"></a> `00bba954` | `00 0c 1e 91` | add x0,x0,#0x783 | `FALL_THROUGH`
<a id="insn-00bba958"></a> `00bba958` | `08 00 00 14` | b 0x00bba978 | `UNCONDITIONAL_JUMP`
<a id="insn-00bba95c"></a> `00bba95c` | `a0 b6 ff f0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bba960"></a> `00bba960` | `00 84 1f 91` | add x0,x0,#0x7e1 | `FALL_THROUGH`
<a id="insn-00bba964"></a> `00bba964` | `41 b7 ff f0` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00bba968"></a> `00bba968` | `21 a0 0c 91` | add x1,x1,#0x328 | `FALL_THROUGH`
<a id="insn-00bba96c"></a> `00bba96c` | `0c 02 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`
<a id="insn-00bba970"></a> `00bba970` | `80 b7 ff f0` | adrp x0,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bba974"></a> `00bba974` | `00 78 1d 91` | add x0,x0,#0x75e | `FALL_THROUGH`
<a id="insn-00bba978"></a> `00bba978` | `41 b7 ff f0` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00bba97c"></a> `00bba97c` | `21 a0 0c 91` | add x1,x1,#0x328 | `FALL_THROUGH`
<a id="insn-00bba980"></a> `00bba980` | `07 02 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba8ec`](#insn-00bba8ec) 範囲 `[['00bba8ec', '00bba8ef']]`
  - `FALL_THROUGH` [`00bba8ec`](#insn-00bba8ec) → [`00bba8f0`](#insn-00bba8f0)
- ブロック [`00bba8f0`](#insn-00bba8f0) 範囲 `[['00bba8f0', '00bba8f3']]`
  - `FALL_THROUGH` [`00bba8f0`](#insn-00bba8f0) → [`00bba8f4`](#insn-00bba8f4)
- ブロック [`00bba8f4`](#insn-00bba8f4) 範囲 `[['00bba8f4', '00bba90f']]`
  - `CONDITIONAL_JUMP` [`00bba90c`](#insn-00bba90c) → [`00bba950`](#insn-00bba950)
  - `FALL_THROUGH` [`00bba90c`](#insn-00bba90c) → [`00bba910`](#insn-00bba910)
- ブロック [`00bba910`](#insn-00bba910) 範囲 `[['00bba910', '00bba91f']]`
  - `FALL_THROUGH` [`00bba91c`](#insn-00bba91c) → [`00bba920`](#insn-00bba920)
- ブロック [`00bba920`](#insn-00bba920) 範囲 `[['00bba920', '00bba92b']]`
  - `CONDITIONAL_JUMP` [`00bba928`](#insn-00bba928) → [`00bba95c`](#insn-00bba95c)
  - `FALL_THROUGH` [`00bba928`](#insn-00bba928) → [`00bba92c`](#insn-00bba92c)
- ブロック [`00bba92c`](#insn-00bba92c) 範囲 `[['00bba92c', '00bba92f']]`
  - `CONDITIONAL_JUMP` [`00bba92c`](#insn-00bba92c) → [`00bba940`](#insn-00bba940)
  - `FALL_THROUGH` [`00bba92c`](#insn-00bba92c) → [`00bba930`](#insn-00bba930)
- ブロック [`00bba930`](#insn-00bba930) 範囲 `[['00bba930', '00bba933']]`
  - `FALL_THROUGH` [`00bba930`](#insn-00bba930) → [`00bba934`](#insn-00bba934)
- ブロック [`00bba934`](#insn-00bba934) 範囲 `[['00bba934', '00bba937']]`
  - `FALL_THROUGH` [`00bba934`](#insn-00bba934) → [`00bba938`](#insn-00bba938)
- ブロック [`00bba938`](#insn-00bba938) 範囲 `[['00bba938', '00bba93f']]`
  - `CONDITIONAL_JUMP` [`00bba93c`](#insn-00bba93c) → [`00bba970`](#insn-00bba970)
  - `FALL_THROUGH` [`00bba93c`](#insn-00bba93c) → [`00bba940`](#insn-00bba940)
- ブロック [`00bba940`](#insn-00bba940) 範囲 `[['00bba940', '00bba94f']]`
- ブロック [`00bba950`](#insn-00bba950) 範囲 `[['00bba950', '00bba95b']]`
  - `UNCONDITIONAL_JUMP` [`00bba958`](#insn-00bba958) → [`00bba978`](#insn-00bba978)
- ブロック [`00bba95c`](#insn-00bba95c) 範囲 `[['00bba95c', '00bba963']]`
  - `FALL_THROUGH` [`00bba960`](#insn-00bba960) → [`00bba964`](#insn-00bba964)
- ブロック [`00bba964`](#insn-00bba964) 範囲 `[['00bba964', '00bba96f']]`
- ブロック [`00bba970`](#insn-00bba970) 範囲 `[['00bba970', '00bba977']]`
  - `FALL_THROUGH` [`00bba974`](#insn-00bba974) → [`00bba978`](#insn-00bba978)
- ブロック [`00bba978`](#insn-00bba978) 範囲 `[['00bba978', '00bba97b']]`
  - `FALL_THROUGH` [`00bba978`](#insn-00bba978) → [`00bba97c`](#insn-00bba97c)
- ブロック [`00bba97c`](#insn-00bba97c) 範囲 `[['00bba97c', '00bba983']]`

## 命令位置別の参照

- [`00bba8f0`](#insn-00bba8f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba8f4`](#insn-00bba8f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba904`](#insn-00bba904) → `010a3700`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba908`](#insn-00bba908) → [`00bde820`](../00bde/00bde820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde820` · 推定シンボル `None` · 推定型 `None`
- [`00bba90c`](#insn-00bba90c) → [`00bba950`](#insn-00bba950) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba920`](#insn-00bba920) → `010a3700`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba924`](#insn-00bba924) → [`00bde830`](../00bde/00bde830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde830` · 推定シンボル `None` · 推定型 `None`
- [`00bba928`](#insn-00bba928) → [`00bba95c`](#insn-00bba95c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba92c`](#insn-00bba92c) → [`00bba940`](#insn-00bba940) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba934`](#insn-00bba934) → `010a3728`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba938`](#insn-00bba938) → [`00be11c0`](../00be1/00be11c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be11c0` · 推定シンボル `None` · 推定型 `None`
- [`00bba93c`](#insn-00bba93c) → [`00bba970`](#insn-00bba970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba940`](#insn-00bba940) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba944`](#insn-00bba944) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba954`](#insn-00bba954) → `00296783`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba958`](#insn-00bba958) → [`00bba978`](#insn-00bba978) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba960`](#insn-00bba960) → `002917e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba968`](#insn-00bba968) → `002a5328`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba96c`](#insn-00bba96c) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`
- [`00bba974`](#insn-00bba974) → `002ad75e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba97c`](#insn-00bba97c) → `002a5328`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba980`](#insn-00bba980) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba8f0`](#insn-00bba8f0)

~~~json
{
  "source": "00bba8f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba8f4`](#insn-00bba8f4)

~~~json
{
  "source": "00bba8f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba904`](#insn-00bba904)

~~~json
{
  "source": "00bba904",
  "target": "010a3700",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba908`](#insn-00bba908)

~~~json
{
  "source": "00bba908",
  "target": "00bde820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba90c`](#insn-00bba90c)

~~~json
{
  "source": "00bba90c",
  "target": "00bba950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba920`](#insn-00bba920)

~~~json
{
  "source": "00bba920",
  "target": "010a3700",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba924`](#insn-00bba924)

~~~json
{
  "source": "00bba924",
  "target": "00bde830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba928`](#insn-00bba928)

~~~json
{
  "source": "00bba928",
  "target": "00bba95c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba92c`](#insn-00bba92c)

~~~json
{
  "source": "00bba92c",
  "target": "00bba940",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba934`](#insn-00bba934)

~~~json
{
  "source": "00bba934",
  "target": "010a3728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba938`](#insn-00bba938)

~~~json
{
  "source": "00bba938",
  "target": "00be11c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba93c`](#insn-00bba93c)

~~~json
{
  "source": "00bba93c",
  "target": "00bba970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba940`](#insn-00bba940)

~~~json
{
  "source": "00bba940",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba944`](#insn-00bba944)

~~~json
{
  "source": "00bba944",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba954`](#insn-00bba954)

~~~json
{
  "source": "00bba954",
  "target": "00296783",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296783",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "2573206661696c656420746f2061637175697265206d7574657800",
  "capture_start": "00296783",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba958`](#insn-00bba958)

~~~json
{
  "source": "00bba958",
  "target": "00bba978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba960`](#insn-00bba960)

~~~json
{
  "source": "00bba960",
  "target": "002917e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917e1",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "2573206661696c656420746f2072656c65617365206d7574657800",
  "capture_start": "002917e1",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba968`](#insn-00bba968)

~~~json
{
  "source": "00bba968",
  "target": "002a5328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5328",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "5f5f6378615f67756172645f61626f727400",
  "capture_start": "002a5328",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba96c`](#insn-00bba96c)

~~~json
{
  "source": "00bba96c",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba974`](#insn-00bba974)

~~~json
{
  "source": "00bba974",
  "target": "002ad75e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad75e",
  "offset": 0,
  "size": 23,
  "datatype": "string",
  "bytes": "2573206661696c656420746f2062726f61646361737400",
  "capture_start": "002ad75e",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba97c`](#insn-00bba97c)

~~~json
{
  "source": "00bba97c",
  "target": "002a5328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5328",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "5f5f6378615f67756172645f61626f727400",
  "capture_start": "002a5328",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba980`](#insn-00bba980)

~~~json
{
  "source": "00bba980",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
