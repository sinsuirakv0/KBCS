# 00b4dbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4dc74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dc74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0067.md#compare-199e738085a5f052d392e0c8494effd8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4dbac",
  "name": "_ZN8firebase9messaging21UnsubscribeLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f34a339f713174c77ab300a55fe87c7ec4b7775dfebfae79fdeb249904136e7",
  "source_text_sha256": "1f34a339f713174c77ab300a55fe87c7ec4b7775dfebfae79fdeb249904136e7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4dbac",
        "00b4dc53"
      ]
    ],
    "bytes_sha256": "c04bc54e38a31cb3f8ba67c1f4d23af96a22e76831cf8ab4b5382c4d7fd0c9f8",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddc80](../00bdd/00bddc80.md)
- [00bddd10](../00bdd/00bddd10.md)
- [00bdddf0](../00bdd/00bdddf0.md)
- [00bdde90](../00bdd/00bdde90.md)
- [00bde080](../00bde/00bde080.md)
- [00be0200](../00be0/00be0200.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1913 bytes

~~~c

void _ZN8firebase9messaging21UnsubscribeLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_010a0fa0 == 0) {
                    /* catch() { ... } // from try @ 00b4c46c with catch @ 00b4dc20 */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
                    /* catch() { ... } // from try @ 00b4c44c with catch @ 00b4dc24 */
    _ZN8firebase5MutexC2ENS0_4ModeE(param_1,0);
                    /* catch() { ... } // from try @ 00b4c418 with catch @ 00b4dc34 */
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* catch() { ... } // from try @ 00b4c3f4 with catch @ 00b4dc38 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
                    /* catch() { ... } // from try @ 00b4d37c with catch @ 00b4dbe0 */
    lVar2 = *(long *)(lVar1 + 0x50);
                    /* catch() { ... } // from try @ 00b4cfe4 with catch @ 00b4dbe4 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC2ENS0_4ModeE(param_1,0);
                    /* catch() { ... } // from try @ 00b4ceec with catch @ 00b4dbf8 */
                    /* catch() { ... } // from try @ 00b4cbe0 with catch @ 00b4dbfc */
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* catch() { ... } // from try @ 00b4c200 with catch @ 00b4dc00 */
                    /* catch() { ... } // from try @ 00b4bee8 with catch @ 00b4dc04 */
    _ZN8firebase12FutureHandleC1Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x80);
  }
                    /* catch() { ... } // from try @ 00b4c7c0 with catch @ 00b4dc48 */
                    /* catch() { ... } // from try @ 00b4c624 with catch @ 00b4dc4c */
                    /* catch() { ... } // from try @ 00b4c3c8 with catch @ 00b4dc50 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4dbac"></a> `00b4dbac` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4dbb0"></a> `00b4dbb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dbb4"></a> `00b4dbb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4dbb8"></a> `00b4dbb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4dbbc"></a> `00b4dbbc` | `89 2a 00 f0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4dbc0"></a> `00b4dbc0` | `29 d1 47 f9` | ldr x9,[x9, #0xfa0] | `FALL_THROUGH`
<a id="insn-00b4dbc4"></a> `00b4dbc4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b4dbc8"></a> `00b4dbc8` | `89 02 00 b4` | cbz x9,0x00b4dc18 | `CONDITIONAL_JUMP`
<a id="insn-00b4dbcc"></a> `00b4dbcc` | `8d 49 02 94` | bl 0x00be0200 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbd0"></a> `00b4dbd0` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b4dbd4"></a> `00b4dbd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b4dbd8"></a> `00b4dbd8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4dbdc"></a> `00b4dbdc` | `d1 3f 02 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbe0"></a> `00b4dbe0` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00b4dbe4"></a> `00b4dbe4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4dbe8"></a> `00b4dbe8` | `d2 3f 02 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbec"></a> `00b4dbec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dbf0"></a> `00b4dbf0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b4dbf4"></a> `00b4dbf4` | `47 40 02 94` | bl 0x00bddd10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbf8"></a> `00b4dbf8` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00b4dbfc"></a> `00b4dbfc` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b4dc00"></a> `00b4dc00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4dc04"></a> `00b4dc04` | `a3 40 02 94` | bl 0x00bdde90 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc08"></a> `00b4dc08` | `c1 02 02 91` | add x1,x22,#0x80 | `FALL_THROUGH`
<a id="insn-00b4dc0c"></a> `00b4dc0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc10"></a> `00b4dc10` | `78 40 02 94` | bl 0x00bdddf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc14"></a> `00b4dc14` | `0c 00 00 14` | b 0x00b4dc44 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4dc18"></a> `00b4dc18` | `20 ba ff d0` | adrp x0,0x293000 | `FALL_THROUGH`
<a id="insn-00b4dc1c"></a> `00b4dc1c` | `00 80 03 91` | add x0,x0,#0xe0 | `FALL_THROUGH`
<a id="insn-00b4dc20"></a> `00b4dc20` | `18 41 02 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc24"></a> `00b4dc24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc28"></a> `00b4dc28` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b4dc2c"></a> `00b4dc2c` | `39 40 02 94` | bl 0x00bddd10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc30"></a> `00b4dc30` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00b4dc34"></a> `00b4dc34` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b4dc38"></a> `00b4dc38` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b4dc3c"></a> `00b4dc3c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4dc40"></a> `00b4dc40` | `10 40 02 94` | bl 0x00bddc80 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc44"></a> `00b4dc44` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4dc48"></a> `00b4dc48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dc4c"></a> `00b4dc4c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4dc50"></a> `00b4dc50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4dbac`](#insn-00b4dbac) 範囲 `[['00b4dbac', '00b4dbcb']]`
  - `CONDITIONAL_JUMP` [`00b4dbc8`](#insn-00b4dbc8) → [`00b4dc18`](#insn-00b4dc18)
  - `FALL_THROUGH` [`00b4dbc8`](#insn-00b4dbc8) → [`00b4dbcc`](#insn-00b4dbcc)
- ブロック [`00b4dbcc`](#insn-00b4dbcc) 範囲 `[['00b4dbcc', '00b4dbdf']]`
  - `FALL_THROUGH` [`00b4dbdc`](#insn-00b4dbdc) → [`00b4dbe0`](#insn-00b4dbe0)
- ブロック [`00b4dbe0`](#insn-00b4dbe0) 範囲 `[['00b4dbe0', '00b4dbe3']]`
  - `FALL_THROUGH` [`00b4dbe0`](#insn-00b4dbe0) → [`00b4dbe4`](#insn-00b4dbe4)
- ブロック [`00b4dbe4`](#insn-00b4dbe4) 範囲 `[['00b4dbe4', '00b4dbf7']]`
  - `FALL_THROUGH` [`00b4dbf4`](#insn-00b4dbf4) → [`00b4dbf8`](#insn-00b4dbf8)
- ブロック [`00b4dbf8`](#insn-00b4dbf8) 範囲 `[['00b4dbf8', '00b4dbfb']]`
  - `FALL_THROUGH` [`00b4dbf8`](#insn-00b4dbf8) → [`00b4dbfc`](#insn-00b4dbfc)
- ブロック [`00b4dbfc`](#insn-00b4dbfc) 範囲 `[['00b4dbfc', '00b4dbff']]`
  - `FALL_THROUGH` [`00b4dbfc`](#insn-00b4dbfc) → [`00b4dc00`](#insn-00b4dc00)
- ブロック [`00b4dc00`](#insn-00b4dc00) 範囲 `[['00b4dc00', '00b4dc03']]`
  - `FALL_THROUGH` [`00b4dc00`](#insn-00b4dc00) → [`00b4dc04`](#insn-00b4dc04)
- ブロック [`00b4dc04`](#insn-00b4dc04) 範囲 `[['00b4dc04', '00b4dc17']]`
  - `UNCONDITIONAL_JUMP` [`00b4dc14`](#insn-00b4dc14) → [`00b4dc44`](#insn-00b4dc44)
- ブロック [`00b4dc18`](#insn-00b4dc18) 範囲 `[['00b4dc18', '00b4dc1f']]`
  - `FALL_THROUGH` [`00b4dc1c`](#insn-00b4dc1c) → [`00b4dc20`](#insn-00b4dc20)
- ブロック [`00b4dc20`](#insn-00b4dc20) 範囲 `[['00b4dc20', '00b4dc23']]`
  - `FALL_THROUGH` [`00b4dc20`](#insn-00b4dc20) → [`00b4dc24`](#insn-00b4dc24)
- ブロック [`00b4dc24`](#insn-00b4dc24) 範囲 `[['00b4dc24', '00b4dc33']]`
  - `FALL_THROUGH` [`00b4dc30`](#insn-00b4dc30) → [`00b4dc34`](#insn-00b4dc34)
- ブロック [`00b4dc34`](#insn-00b4dc34) 範囲 `[['00b4dc34', '00b4dc37']]`
  - `FALL_THROUGH` [`00b4dc34`](#insn-00b4dc34) → [`00b4dc38`](#insn-00b4dc38)
- ブロック [`00b4dc38`](#insn-00b4dc38) 範囲 `[['00b4dc38', '00b4dc43']]`
  - `FALL_THROUGH` [`00b4dc40`](#insn-00b4dc40) → [`00b4dc44`](#insn-00b4dc44)
- ブロック [`00b4dc44`](#insn-00b4dc44) 範囲 `[['00b4dc44', '00b4dc47']]`
  - `FALL_THROUGH` [`00b4dc44`](#insn-00b4dc44) → [`00b4dc48`](#insn-00b4dc48)
- ブロック [`00b4dc48`](#insn-00b4dc48) 範囲 `[['00b4dc48', '00b4dc4b']]`
  - `FALL_THROUGH` [`00b4dc48`](#insn-00b4dc48) → [`00b4dc4c`](#insn-00b4dc4c)
- ブロック [`00b4dc4c`](#insn-00b4dc4c) 範囲 `[['00b4dc4c', '00b4dc4f']]`
  - `FALL_THROUGH` [`00b4dc4c`](#insn-00b4dc4c) → [`00b4dc50`](#insn-00b4dc50)
- ブロック [`00b4dc50`](#insn-00b4dc50) 範囲 `[['00b4dc50', '00b4dc53']]`

## 命令位置別の参照

- [`00b4dbac`](#insn-00b4dbac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbb0`](#insn-00b4dbb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbb4`](#insn-00b4dbb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbc0`](#insn-00b4dbc0) → `010a0fa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dbc8`](#insn-00b4dbc8) → [`00b4dc18`](#insn-00b4dc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbcc`](#insn-00b4dbcc) → [`00be0200`](../00be0/00be0200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0200` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbdc`](#insn-00b4dbdc) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbe8`](#insn-00b4dbe8) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbf4`](#insn-00b4dbf4) → [`00bddd10`](../00bdd/00bddd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd10` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc04`](#insn-00b4dc04) → [`00bdde90`](../00bdd/00bdde90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde90` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc10`](#insn-00b4dc10) → [`00bdddf0`](../00bdd/00bdddf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddf0` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc14`](#insn-00b4dc14) → [`00b4dc44`](#insn-00b4dc44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc1c`](#insn-00b4dc1c) → `002930e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4dc20`](#insn-00b4dc20) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc2c`](#insn-00b4dc2c) → [`00bddd10`](../00bdd/00bddd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd10` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc40`](#insn-00b4dc40) → [`00bddc80`](../00bdd/00bddc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc80` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc44`](#insn-00b4dc44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc48`](#insn-00b4dc48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4dbac`](#insn-00b4dbac)

~~~json
{
  "source": "00b4dbac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbb0`](#insn-00b4dbb0)

~~~json
{
  "source": "00b4dbb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbb4`](#insn-00b4dbb4)

~~~json
{
  "source": "00b4dbb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbc0`](#insn-00b4dbc0)

~~~json
{
  "source": "00b4dbc0",
  "target": "010a0fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0fa0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dbc8`](#insn-00b4dbc8)

~~~json
{
  "source": "00b4dbc8",
  "target": "00b4dc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbcc`](#insn-00b4dbcc)

~~~json
{
  "source": "00b4dbcc",
  "target": "00be0200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbdc`](#insn-00b4dbdc)

~~~json
{
  "source": "00b4dbdc",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbe8`](#insn-00b4dbe8)

~~~json
{
  "source": "00b4dbe8",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbf4`](#insn-00b4dbf4)

~~~json
{
  "source": "00b4dbf4",
  "target": "00bddd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc04`](#insn-00b4dc04)

~~~json
{
  "source": "00b4dc04",
  "target": "00bdde90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc10`](#insn-00b4dc10)

~~~json
{
  "source": "00b4dc10",
  "target": "00bdddf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc14`](#insn-00b4dc14)

~~~json
{
  "source": "00b4dc14",
  "target": "00b4dc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc1c`](#insn-00b4dc1c)

~~~json
{
  "source": "00b4dc1c",
  "target": "002930e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002930e0",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002930e0",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4dc20`](#insn-00b4dc20)

~~~json
{
  "source": "00b4dc20",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc2c`](#insn-00b4dc2c)

~~~json
{
  "source": "00b4dc2c",
  "target": "00bddd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc40`](#insn-00b4dc40)

~~~json
{
  "source": "00b4dc40",
  "target": "00bddc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc44`](#insn-00b4dc44)

~~~json
{
  "source": "00b4dc44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc48`](#insn-00b4dc48)

~~~json
{
  "source": "00b4dc48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
