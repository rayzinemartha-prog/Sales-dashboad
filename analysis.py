{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1824fc4d-08d2-420c-b6da-603e88b7d8a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_csv(\"sales_analytics_dataset-1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "95622a0e-ce33-4920-8a11-d84a2f87558a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order_ID</th>\n",
       "      <th>Order_Date</th>\n",
       "      <th>Region</th>\n",
       "      <th>City</th>\n",
       "      <th>Customer_Segment</th>\n",
       "      <th>Product</th>\n",
       "      <th>Category</th>\n",
       "      <th>Sub_Category</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Unit_Price</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Profit</th>\n",
       "      <th>Payment_Method</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ORD-00494</td>\n",
       "      <td>2025-01-01</td>\n",
       "      <td>Central</td>\n",
       "      <td>Kampala</td>\n",
       "      <td>Small Business</td>\n",
       "      <td>Stapler</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Tools</td>\n",
       "      <td>5</td>\n",
       "      <td>15.94</td>\n",
       "      <td>0.05</td>\n",
       "      <td>75.72</td>\n",
       "      <td>17.73</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ORD-00657</td>\n",
       "      <td>2025-01-01</td>\n",
       "      <td>Central</td>\n",
       "      <td>Kampala</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>Whiteboard</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Boards</td>\n",
       "      <td>3</td>\n",
       "      <td>102.03</td>\n",
       "      <td>0.00</td>\n",
       "      <td>306.09</td>\n",
       "      <td>76.94</td>\n",
       "      <td>Card</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ORD-00415</td>\n",
       "      <td>2025-01-02</td>\n",
       "      <td>Northern</td>\n",
       "      <td>Arua</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>Office Desk</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Tables</td>\n",
       "      <td>3</td>\n",
       "      <td>388.52</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1165.56</td>\n",
       "      <td>202.19</td>\n",
       "      <td>Bank Transfer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ORD-00799</td>\n",
       "      <td>2025-01-02</td>\n",
       "      <td>Western</td>\n",
       "      <td>Mbarara</td>\n",
       "      <td>Small Business</td>\n",
       "      <td>Notebook Pack</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Paper</td>\n",
       "      <td>2</td>\n",
       "      <td>16.68</td>\n",
       "      <td>0.15</td>\n",
       "      <td>28.36</td>\n",
       "      <td>5.82</td>\n",
       "      <td>Mobile Money</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ORD-01107</td>\n",
       "      <td>2025-01-02</td>\n",
       "      <td>Central</td>\n",
       "      <td>Mukono</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Office Desk</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Tables</td>\n",
       "      <td>1</td>\n",
       "      <td>409.54</td>\n",
       "      <td>0.10</td>\n",
       "      <td>368.59</td>\n",
       "      <td>50.87</td>\n",
       "      <td>Cash</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Order_ID  Order_Date    Region     City Customer_Segment        Product  \\\n",
       "0  ORD-00494  2025-01-01   Central  Kampala   Small Business        Stapler   \n",
       "1  ORD-00657  2025-01-01   Central  Kampala         Consumer     Whiteboard   \n",
       "2  ORD-00415  2025-01-02  Northern     Arua         Consumer    Office Desk   \n",
       "3  ORD-00799  2025-01-02   Western  Mbarara   Small Business  Notebook Pack   \n",
       "4  ORD-01107  2025-01-02   Central   Mukono        Corporate    Office Desk   \n",
       "\n",
       "          Category Sub_Category  Quantity  Unit_Price  Discount    Sales  \\\n",
       "0  Office Supplies        Tools         5       15.94      0.05    75.72   \n",
       "1  Office Supplies       Boards         3      102.03      0.00   306.09   \n",
       "2        Furniture       Tables         3      388.52      0.00  1165.56   \n",
       "3  Office Supplies        Paper         2       16.68      0.15    28.36   \n",
       "4        Furniture       Tables         1      409.54      0.10   368.59   \n",
       "\n",
       "   Profit Payment_Method  \n",
       "0   17.73           Card  \n",
       "1   76.94           Card  \n",
       "2  202.19  Bank Transfer  \n",
       "3    5.82   Mobile Money  \n",
       "4   50.87           Cash  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "98264969-3516-4cb1-be8f-3b78c30072f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1200, 14)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a2eb44dc-8865-4974-bbc5-fe60bb6c3b6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Order_ID            0\n",
       "Order_Date          0\n",
       "Region              0\n",
       "City                0\n",
       "Customer_Segment    0\n",
       "Product             0\n",
       "Category            0\n",
       "Sub_Category        0\n",
       "Quantity            0\n",
       "Unit_Price          0\n",
       "Discount            0\n",
       "Sales               0\n",
       "Profit              0\n",
       "Payment_Method      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "909ae579-ced8-40f0-870d-c6277efc9e8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Sales: 807909.9700000001\n",
      "Total Profit: 134890.72\n",
      "Total Quantity: 3446\n",
      "Number of Orders: 1200\n"
     ]
    }
   ],
   "source": [
    "print(\"Total Sales:\",\n",
    "df[\"Sales\"].sum())\n",
    "print(\"Total Profit:\",\n",
    "df[\"Profit\"].sum())\n",
    "print(\"Total Quantity:\",\n",
    "df[\"Quantity\"].sum())\n",
    "print(\"Number of Orders:\",\n",
    "df[\"Order_ID\"].nunique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4554f8a1-5347-4ec9-a8f4-c477ab63eeda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Category\n",
      "Furniture          29431.71\n",
      "Office Supplies     6559.70\n",
      "Technology         98899.31\n",
      "Name: Profit, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "category_profit= df.groupby(\"Category\")[\"Profit\"].sum()\n",
    "print(category_profit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "43f290cb-44ce-490f-80ce-a379cdd94475",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Region\n",
      "Central     319657.81\n",
      "Eastern     156787.27\n",
      "Northern    167411.38\n",
      "Western     164053.51\n",
      "Name: Sales, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "region_sales= df.groupby(\"Region\")[\"Sales\"].sum()\n",
    "print(region_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "62dbb9eb-f47a-4b59-884c-be2fa5c1ac68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Sales')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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SRMnd4eKqqioSF9++aW6deumOnXqaPHixZoyZYoOHTqkPXv2KDg4WA8++KCz27xu8V2BcClVq1ZVdna26tWr5zC+YcMG1a5d20ldoaIaNWqUQkNDtX//fj344IP272Nzc3PT8OHDndwdKqJBgwbp888/lyQ98sgjGj9+vEJDQ+3bvb29NW7cONWtW9dJHV7/CFZwKVFRURo2bJhmz54ti8WikpIS/fDDDxo6dKgeffRRZ7eHCuiBBx6QJJ05c8Y+1rdvX2e1gwpuy5Ytmjx5su6//36H6RK/FxQUpO++++4ad1Zx8CXMcClFRUWKiYlRUlKSDMOQu7u7iouLFRUVpcTEROa14JoqLi5WfHy83nvvPR06dEg7duxQ/fr19fLLL6tu3brq16+fs1sEcI0RrOAyDMPQvn37VLNmTeXk5Gj9+vUqKSnRLbfcokaNGjm7PVRAY8aM0SeffKIxY8aof//+ysrKUv369fXFF19o4sSJ3FCBa+6bb7654LjFYtENN9yghg0blplKAXMRrOAySkpKdMMNN2jz5s0EKZQLDRs21Pvvv6+OHTvKx8dHP/74o+rXr69t27YpLCyMFdhxzVWqVEkWi0Xn/2kvHbNYLLrzzjs1b948+fn5OanL6xt3BcJlVKpUSY0aNeLuP5Qbv/zyixo2bFhmvKSkREVFRU7oCBVdamqqbrvtNqWmpiovL095eXlKTU3V7bffrm+//Vbff/+9jh07pqFDhzq71esWk9fhUsaPH6/nn39eU6dOdbjTBXCG5s2ba/ny5apTp47D+OzZs3XLLbc4qStUZM8++6w++OADtW3b1j7WsWNH3XDDDXryySe1efNmTZo0SY8//rgTu7y+EazgUh555BH99ttvuummm+Tp6SkvLy+H7b/++quTOkNFNHLkSEVHR+uXX35RSUmJ5syZo+3bt2v69On69ttvnd0eKqBdu3bJ19e3zLivr692794tSWrUqJGOHj16rVurMAhWcCmTJk1ydguAXc+ePTVr1izFx8fLYrHolVde0a233qr58+fbFwsFrqVWrVrp+eef1/Tp01WzZk1J0pEjR/TCCy/otttukyTt3LlTN954ozPbvK4xeR0AgOvE9u3bde+999pXWLdYLNq3b5/q16+vr7/+Wo0bN9a8efN04sQJRUdHO7vd6xLBCi5l3759F93+t7/97Rp1AgDl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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#pip install matplotlib#\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "category_sales=df.groupby(\"Category\")[\"Sales\"].sum()\n",
    "category_sales.plot(kind=\"bar\")\n",
    "plt.title(\"Sales by Category\")\n",
    "plt.xlabel(\"Category\")\n",
    "plt.ylabel(\"Sales\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "49a32215-4b38-4c1b-a5ee-44afac790244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Order_ID                    object\n",
      "Order_Date          datetime64[ns]\n",
      "Region                      object\n",
      "City                        object\n",
      "Customer_Segment            object\n",
      "Product                     object\n",
      "Category                    object\n",
      "Sub_Category                object\n",
      "Quantity                     int64\n",
      "Unit_Price                 float64\n",
      "Discount                   float64\n",
      "Sales                      float64\n",
      "Profit                     float64\n",
      "Payment_Method              object\n",
      "Order_date          datetime64[ns]\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "df[\"Order_Date\"]=pd.to_datetime(df[\"Order_Date\"])\n",
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "26170ef8-9e5c-4af1-aca8-a79af4c480d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate rows: 0\n"
     ]
    }
   ],
   "source": [
    "print(\"Number of duplicate rows:\",\n",
    "df.duplicated().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "39d29c30-8b8f-4edf-a093-02e7a57031aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total sales: 807909.9700000001\n",
      "Total profit: 134890.72\n",
      "Total Quantity: 3446\n",
      "Total Orders: 1200\n"
     ]
    }
   ],
   "source": [
    "total_sales= df[\"Sales\"].sum()\n",
    "total_profit= df[\"Profit\"].sum()\n",
    "total_quantity= df[\"Quantity\"].sum()\n",
    "total_orders= df[\"Order_ID\"].nunique()\n",
    "\n",
    "print(\"Total sales:\", total_sales)\n",
    "print(\"Total profit:\", total_profit)\n",
    "print(\"Total Quantity:\", total_quantity)\n",
    "print(\"Total Orders:\", total_orders)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "31c4f42c-0e1c-45e6-8a63-e5b865c37ab5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sales by Category:\n",
      "Category\n",
      "Furniture          209848.68\n",
      "Office Supplies     28305.70\n",
      "Technology         569755.59\n",
      "Name: Sales, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "sales_by_category= df.groupby(\"Category\")[\"Sales\"].sum()\n",
    "print(\"\\nSales by Category:\")\n",
    "print(sales_by_category)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c2f704d0-3a8e-447a-9f60-885611f5cc1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sales by Region:\n",
      "Region\n",
      "Central     319657.81\n",
      "Eastern     156787.27\n",
      "Northern    167411.38\n",
      "Western     164053.51\n",
      "Name: Sales, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "sales_by_region=df.groupby(\"Region\")[\"Sales\"].sum()\n",
    "print(\"\\nSales by Region:\")\n",
    "print(sales_by_region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c6123be2-329c-453e-bdc3-c079222adbd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Monthly Sales:\n",
      "Order_date\n",
      "2025-01    86919.72\n",
      "2025-02    45436.80\n",
      "2025-03    67443.82\n",
      "2025-04    81153.90\n",
      "2025-05    56761.96\n",
      "2025-06    79713.28\n",
      "2025-07    57481.40\n",
      "2025-08    83962.54\n",
      "2025-09    56045.20\n",
      "2025-10    59683.69\n",
      "2025-11    59966.30\n",
      "2025-12    73341.36\n",
      "Freq: M, Name: Sales, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "monthly_sales=(df.groupby(df[\"Order_date\"].dt.to_period(\"M\"))[\"Sales\"].sum())\n",
    "print(\"\\nMonthly Sales:\")\n",
    "print(monthly_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c37434c-7a48-47f6-ad58-94d562725d01",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
